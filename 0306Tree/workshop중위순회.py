import sys
sys.stdin = open("workshop중위순회_input.txt")

tc = 10

def inorder(node):
    if node != 0:
        inorder(tree[node][1])
        print(tree[node][0], end="")
        inorder(tree[node][2])

def printTree():
    for i in range(1, N+1):
        print("%2d %2s %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2], tree[i][3]))

for T in range(tc):
    N = int(input())
    tree = [[0 for _ in range(4)] for _ in range(N + 1)]
    # i, alpha, left, right, parent
    #      0     1      2      3
    for n in range(N):
        data = list(input().split())
        # print(data)
        if len(data) == 4:
            n1 = int(data[0]) # node
            n2 = data[1] # alpha
            n3 = int(data[2]) # lef
            n4 = int(data[3]) # rig

            if tree[n1][1] == 0:
                tree[n1][1] = n3
            if tree[n1][2] == 0:
                tree[n1][2] = n4
            tree[n1][3] = int(n1//2)
            tree[n1][0] = n2

        elif len(data) == 3:
            n1 = int(data[0])  # node
            n2 = data[1]  # alpha
            n3 = int(data[2])  # lef

            if tree[n1][1] == 0:
                tree[n1][1] = n3
            tree[n1][3] = int(n1 // 2)
            tree[n1][0] = n2
        elif len(data) == 2:
            n1 = int(data[0])  # node
            n2 = data[1]  # alpha
            tree[n1][3] = int(n1 // 2)
            tree[n1][0] = n2
    # printTree()
    print("%s%d" % ('#', T+1), end=" ")
    inorder(1)
    print()