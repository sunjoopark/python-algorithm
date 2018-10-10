table = [0 for i in range(200)]
n = 0
def f(k):
    if k == n + 1:
        return 0
    table[k] = k + f(k + 1)
    return table[k]

if __name__ == "__main__":
    n = 100
    print("%d"%(f(1)))