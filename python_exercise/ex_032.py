def f():
    a = ord('A')
    while a <= ord('Z'):
        b = ord('A')
        while b <= (ord('Z') - (a - 65)):
            print("%2c"%(b),end="")
            b = b + 1
        print()
        a = a + 1

if __name__ == "__main__":
    f()