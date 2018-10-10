a = [0] * 101
def calc_array(n):
    a[1] = 1
    i = 2
    while i <= n:
        a[i] = a[i // 2] + 1
        i = i + 1

if __name__ == "__main__":
    calc_array(100)
    i = 0
    while i <= 100:
        print(" {0} ".format(a[i]), end="")
        i = i + 1