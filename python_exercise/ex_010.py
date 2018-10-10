def solve(n):
    ans = 0
    i = 1
    while i <= n:
        if n % i == 0:
            print("약수 : {0}".format(i))
        i = i + 1

if __name__ == "__main__":
    n = int(input("입력:"))
    solve(n)