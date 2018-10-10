def f(n):
    a = [0] * 100
    i = 1
    while i <= n:
        a[i] = 0
        i = i + 1
    i = 1
    while i <= n:
        j = i
        while j <= n:
            a[j] = 1 - a[j]
            j = j + i
        i = i + 1
    cnt = 0
    i = 1
    while i <= n:
        if a[i] == 1:
            cnt = cnt + 1
        i = i + 1
    return cnt

if __name__ == "__main__":
    print("10의 제곱근 : %d"%(f(10)))