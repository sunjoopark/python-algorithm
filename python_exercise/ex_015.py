def calc_prime_factorization(n):
    i = 2
    while i <= n:
        while 1:
            if n % i == 0:
                print(i)
                n = n // i
            else :
                break
        i = i + 1

if __name__ == "__main__":
    calc_prime_factorization(48)