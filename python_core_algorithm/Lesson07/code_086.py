#!/usr/bin/python
#트리에서 사용할 노드(Node) 클래스의 선언
class Node:
    def __init__(self, data ):
        self.data = data
        self.left = None
        self.right = None

#전위 순회 알고리즘(Preorder Traverse)
def preorder_traverse(node):
    if node == None: return
    print(node.data , end = ' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

#중위 순회 알고리즘(Inorder Traverse)
def inorder_traverse(node):
    if node == None: return
    inorder_traverse(node.left)
    print(node.data , end = ' -> ')
    inorder_traverse(node.right)

#후위 순회 알고리즘(Postorder Traverse)
def postorder_traverse(node):
    if node == None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data , end = ' -> ')

root = None
#트리의 초기화
def init_tree():
    global root
    new_node = Node("A")
    root = new_node
    new_node = Node("B")
    root.left = new_node
    new_node = Node("C")
    root.right = new_node
    new_node_1 = Node("D")
    new_node_2 = Node("E")
    node = root.left
    node.left = new_node_1
    node.right = new_node_2
    new_node_1 = Node("F")
    new_node_2 = Node("G")
    node = root.right
    node.left = new_node_1
    node.right = new_node_2

levelq = []
#단계 순위 순회 알고리즘(Leveorder Traverse)
def levelorder_traverse(node):
    global levelq
    levelq.append(node)
    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data , end = ' -> ')
        # child put
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)

#순회 프로그램의 시작점
if __name__ == '__main__':
    init_tree()
    print("< Preorder Traverse >")
    preorder_traverse(root)
    print("\n")
    print("< Inorder Traverse >")
    inorder_traverse(root)
    print("\n")
    print("< Postorder Traverse >")
    postorder_traverse(root)
    print("\n")
    print("< Leveorder Traverse >")
    levelorder_traverse(root)
    print("\n")