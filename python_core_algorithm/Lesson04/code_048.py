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

def insert_node(data):
    global node_A

    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node
    new_node.prev = node_P
    node_T.prev = new_node

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

if __name__ == '__main__':
    print("연결 리스트 초기화 후")
    init_list()
    print_list()
    print("노드 C의 추가 후")
    insert_node("C")
    print_list()