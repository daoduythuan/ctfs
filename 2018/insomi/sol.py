import string

s = "ADFOMWL0AGTNYW1OATBTMW1PBXHVC3LNAMFHBWP0ZTZOZ3D0CWPLDWZ6A256D3KYANHXBNF6YWHVDW14ANFVEQ==".decode("base64")


def enc(f):
    f = f.encode("base64")
    f = f.encode("base64")
    f = f.lower()
    f = f.encode("rot13")
    f = f.encode("base64")
    f = f.upper()
    f = f.decode("base64")
    return f


def brute(flg, score):
    print(flg, score)
    for c in string.letters + string.digits + "{}_":
        m = get_score(flg + c)
        if m > score:
            brute(flg + c, m)


def get_score(flg):
    f = enc(flg)
    m = -1
    for i in range(len(f)):
        if f[:i] == s[:i]:
            m = i
    return m


def main():
    flag = "INS{"
    score = get_score(flag)
    brute(flag, score)


main()
