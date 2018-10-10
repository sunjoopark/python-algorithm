def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("{0}는 소수".format(n))
    else:
        print("{0}는 합성수".format(n))

if __name__ == "__main__":
    i = 2
    while i <= 20:
        check_prime(i)
        i = i + 1