def solve(n):
    ans = 0
    i = 1
    while i <= n:
        if n % i == 0:
            ans = ans + i
        i = i + 1
    return ans

if __name__ == "__main__":
    n = int(input("입력 : "))
    print("약수의합 : {0}".format(solve(n)))