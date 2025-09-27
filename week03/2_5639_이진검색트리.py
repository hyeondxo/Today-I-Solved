import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

pre = list(map(int, input().split()))
output = []


def postorder(start, end):
    if start >= end:
        return

    root = pre[start]
    mid = start + 1
    while mid < end and pre[mid] < root:
        mid += 1

    postorder(start + 1, mid)
    postorder(mid, end)
    output.append(str(root))


postorder(0, len(pre))
sys.stdout.write('\n'.join(output))

# pypy3 메모리 초과, python3 통과
# def postorder(start, end):
#     if start >= end:
#         return
#     root = pre[start]

#     mid = start + 1
#     while mid < end and pre[mid] < root:
#         mid += 1
#     postorder(start + 1, mid)
#     postorder(mid, end)
#     result.append(root)


# pre = []
# result = []
# while True:
#     val = input().strip()
#     if not val:
#         break
#     pre.append(int(val))

# postorder(0, len(pre))
# sys.stdout.write("\n".join(map(str, result)))


# python3 시간초과, pypy3 메모리 초과
# def insert(tree, root, val):
#     if root not in tree:
#         tree[root] = [None, None]
#     if val < root:
#         if tree[root][0] is None:
#             tree[root][0] = val
#         else:
#             insert(tree, tree[root][0], val)
#     else:
#         if tree[root][1] is None:
#             tree[root][1] = val
#         else:
#             insert(tree, tree[root][1], val)


# def postorder(tree, node):
#     if node is None:
#         return
#     if node in tree:
#         postorder(tree, tree[node][0])
#         postorder(tree, tree[node][1])
#     print(node)


# pre = []
# while True:
#     value = input().strip()
#     if not value:
#         break
#     pre.append(int(value))

# tree = {}
# root = pre[0]
# for i in range(1, len(pre)):
#     insert(tree, root, pre[i])

# postorder(tree, root)


# pypy3 메모리 초과, python3 시간 초과
# class Tree:
#     def __init__(self, node):
#         self.node = node
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if value < self.node:
#             if self.left is None:
#                 self.left = Tree(value)
#             else:
#                 self.left.insert(value)
#         else:  # 입력 값이 현재 노드보다 클 때
#             if self.right is None:
#                 self.right = Tree(value)
#             else:
#                 self.right.insert(value)

#     def postorder(self, result):
#         if self.left:
#             self.left.postorder(result)
#         if self.right:
#             self.right.postorder(result)
#         result.append(self.node)


# preorder = list(map(int, sys.stdin.read().split()))
# tree = Tree(preorder[0])
# for value in preorder[1:]:
#     tree.insert(value)

# result = []
# tree.postorder(result)
# sys.stdout.write("\n".join(map(str, result)))
