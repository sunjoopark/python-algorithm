def calc_LCM(n):
    a = 2
    b = 3
    c = 5
    i = 2
    while i < n:
        if (i % a == 0) and (i % b == 0) and (i % c == 0):
            break
        i = i + 1
    print("2, 3 ,5의 최소공배수 : {0}".format(i))

if __name__ == "__main__":
    calc_LCM(100)