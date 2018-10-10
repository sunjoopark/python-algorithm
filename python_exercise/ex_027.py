def fact(n):
    fact = 1
    i = n
    while i > 1:
        fact = fact * i
        i = i - 1
    return fact
if __name__ == "__main__":
    for i in range(21):
        print("%2d! = %20d"%(i,fact(i)))