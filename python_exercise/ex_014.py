def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p%q)

if __name__ == "__main__":
    r = gcd(24, 64)
    print("24와 64의 최대공약수 : {0}".format(r))