str ="mississippi"
length = 11
def f():
    p = 0
    c = 0
    for i in range(length):
        j = i + 1
        while j < length :
            p = j - i +1
            k = 0
            while i + k < j - k:
                if str[i+k] != str[j-k]:
                    p = 0
                    break
                k = k + 1
            c = c + p
            j = j + 1
    print("회문의 갯수 : %d"%(c))
if __name__ == "__main__":
    f()