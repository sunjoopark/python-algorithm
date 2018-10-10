def fib(n):
    a = 1
    b = 1
    for k in range(3,n) :
        dummy = b
        b = a + b
        a = dummy
    return b

if __name__ == "__main__":
    for i in range(41) :
        print("피보나치 %2d = %10d"%(i, fib(i)))