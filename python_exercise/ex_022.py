def f(k,m):
    if k <= 1:
        return 1 % m
    else:
        return (f(k - 1,m) + 2 * f(k - 2,m)) % m

if __name__ == "__main__":
    n = int(input("n : ")) # n = 8
    m = int(input("m : ")) # m = 100
    print(f(n,m))