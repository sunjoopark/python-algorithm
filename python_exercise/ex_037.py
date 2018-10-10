N = 12
def combi(n, r):
    p = 1
    for i in range(1,r) :
        p = p*(n - i + 1) // i
    return p

if __name__ == "__main__":
    for n in range(N+1) :
        t = 0
        while t < (N - n) * 3 :
            print(" ",end="")
            t = t + 1
        for r in range(n + 1) :
            print("%3d "%(combi(n,r)), end="")
        print()