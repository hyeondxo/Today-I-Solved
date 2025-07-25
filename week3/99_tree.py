# 1. 노드 클래스 - 실제 데이터를 담음
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 2. 트리 클래스 - 노드들을 관리
class Tree:
    def __init__(self):
        self.nodes = {}  # 노드 이름을 문자(키)로 하고, Node 객체를 값으로 저장하는 딕셔너리

    def add(self, data, left, right):
        self.nodes[data] = Node(data, left, right)

    def preorder(self, node):  # 전위 순회 : root -> left -> right
        if node:
            print(node, end="")
            self.preorder(self.nodes[node].left)
            self.preorder(self.nodes[node].right)

    def inorder(self, node):  # 중위 순회 : left -> root -> right
        if node:
            self.inorder(self.nodes[node].left)
            print(node, end="")
            self.inorder(self.nodes[node].right)

    def postorder(self, node):  # 후위 순회 : right -> left -> root
        if node:
            self.postorder(self.nodes[node].left)
            self.postorder(self.nodes[node].right)
            print(node, end="")
