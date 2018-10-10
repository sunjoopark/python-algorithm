def abs(a, b):
    if a > b:
        return a - b
    else:
        return b - a

if __name__ == "__main__":
    a = -15
    b = 77
    print("|{0} - {1}| = {2}".format(a,b,abs(a,b)))