def combi(n,r):
    if r == 0 or r == n:
        return 1
    else:
        return combi(n-1,r) + combi(n -1, r -1)

if __name__ == "__main__":
    n = 0
    while n <= 5:
        r = 0
        while r <= n:
            print(" {0} C {1} = {2} ".format(n,r,combi(n,r)), end="")
            r = r + 1
        n = n + 1
        print()