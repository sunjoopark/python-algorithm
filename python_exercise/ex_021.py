def combi(n,r):
    if r == n:
        return 1
    elif r == 1:
        return n
    else:
        return combi(n,r-1)*(n-r+1)//r

if __name__ == "__main__":
    n = 1
    while n <= 5:
        r = 1
        while r <= n:
            print(" {0} C {1} = {2} ".format(n,r,combi(n,r)), end="")
            r = r + 1
        n = n + 1
        print()