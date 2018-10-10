def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for i in range(41) :
        print("피보나치 %2d = %10d"%(i, fib(i)))