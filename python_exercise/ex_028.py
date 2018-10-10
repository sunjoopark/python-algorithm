def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

if __name__ == "__main__":
    for i in range(21):
        print("%2d! = %20d"%(i,fact(i)))