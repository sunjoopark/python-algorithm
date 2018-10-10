d = "0123456789ABCDEFGHIJ"
def f(n, k):
    if n > 0 :
        f(n // k, k)
        print("%c"%d[n%k], end="")
if __name__ == "__main__":
    n = int(input("변환할 10진수 입력 :"))
    k = int(input("변환진수 입력 :"))
    f(n,k)