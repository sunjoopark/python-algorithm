from math import log10
from random import randint

def get_digit(number, base, pos):
    return (number // base ** pos) % base

def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i-1]
    return array

def radixsort(l, base=10):
    passes = int(log10(max(l))+1)
    output = [0] * len(l)
    for pos in range(passes):
        count = [0] * base
        for i in l:
            digit = get_digit(i, base, pos)
            count[digit] +=1
        count = prefix_sum(count)
        for i in reversed(l):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos] = i
        l = list(output)
    return output

if __name__ == '__main__':
    l = []
    l = [ randint(1, 99999) for x in range(100) ]
    print("< 정렬 전 >")
    print(l)
    sorted = radixsort(l)
    print("< 정렬 후 >")
    print(sorted)