def gcd(p, q):
    if p > q :
        a = p
        b = q
    else:
        a = q
        b = p
    while b > 0:
        c = b
        b = a % b
        a = c
    return a

if __name__ == "__main__":
    r = gcd(24, 64)
    print("24와 64의 최대공약수 : {0}".format(r))