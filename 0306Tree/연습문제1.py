def preorder(node): # 1을 집어넣음
    if node != 0: # node 값이 0이 아니면 들어간다.
        print(node, end=" ") # 1
        preorder(tree[node][0]) # 1의 left
        preorder(tree[node][1]) # 1의 right


def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=" ")
        inorder(tree[node][1])


def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")

def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

import sys
sys.stdin = open("input.txt")
V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)] # Left, Right, Parent
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i * 2] # left
    n2 = temp[i * 2 + 1] # right
    if tree[n1][0] == 0:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

printTree()
preorder(1)
print()
inorder(1)
print()
postorder(1)