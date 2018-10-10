a = [1] * 100
def calc_array(n):
    a[1] = 1
    a[2] = 1
    i = 3
    while i <= n:
        a[i] = a[i-1] + a[i -2] + 1
        i = i + 1

if __name__ == "__main__":
    calc_array(10)
    i = 0
    while i <= 7:
        print(a[i])
        i = i + 1