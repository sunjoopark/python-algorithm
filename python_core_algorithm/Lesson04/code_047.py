#!/usr/bin/python
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_B.prev = node_A
    node_D.next = node_E
    node_D.prev = node_B

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

if __name__ == '__main__':
    print("연결리스트 초기화 후")
    init_list()
    print_list()