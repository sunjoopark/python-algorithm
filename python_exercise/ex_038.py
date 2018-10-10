def f(a, b):
    if b == 0 :
        return a
    else:
        return f(b, a % b)
if __name__ == "__main__":
    print("84 and 60 : %d\n"%(f(84, 60)))