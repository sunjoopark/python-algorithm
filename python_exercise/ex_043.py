table = [0 for i in range(200)]
if __name__ == "__main__":
    n = 100
    for i in range(n+1) :
        if i == 1:
            table[i] = 1
        else:
            table[i] = table[i - 1] + i
    print("%d"%(table[n]))