#!/usr/bin/python
import random
from math import log10

def left_node(idx=None):
    return ((idx + 1) << 1) - 1

def right_node(idx=None):
    return (idx + 1) << 1

def up_heap(mylist=None, idx=None, heap_size=None):
    l_node = left_node(idx)
    r_node = right_node(idx)
    if l_node <= heap_size and mylist[l_node] > mylist[idx]:
        largest = l_node
    else:
        largest = idx
    if r_node <= heap_size and mylist[r_node] > mylist[largest]:
        largest = r_node
    if largest != idx:
        mylist[idx], mylist[largest] = mylist[largest], mylist[idx]
        up_heap(mylist, largest, heap_size)


def build_heap(mylist=None):
    heap_size = len(mylist) - 1
    for i in reversed(range(len(mylist) // 2)):
        up_heap(mylist, i, heap_size)

def heap_sort(heap=None):
    tmp_arry = list()
    for i in range(len(heap)):
        tmp_arry.append(heap.pop(0))
        up_heap(heap, 0, len(heap) - 1)
    return tmp_arry

if __name__ == '__main__':
    data = []
    input_n = input("정렬할 데이터의 수 : ")
    data = [random.randint(1, 99999) for x in range(int(input_n))]
    print("< 정렬 전 >")
    print(data)
    build_heap(data)
    sorted_data = heap_sort(data)
    print("< 정렬 후 >")
    print(sorted_data)