TRUE = 1
FALSE = 0
def calc_prime(n):
    check = [TRUE] * 1000
    cnt = 0
    i = 2
    k = 1
    while i < n:
        if check[i] == TRUE:
            print(i)
            j = 1
            while j < n:
                check[j] = FALSE
                k = k + 1
                j = i * k
            k = 1
        i = i + 1

if __name__ == "__main__":
    n = 20
    calc_prime(n)