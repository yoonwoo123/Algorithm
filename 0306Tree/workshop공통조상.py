import sys
sys.stdin = open("workshop공통조상_input.txt")


def printTree():
    for i in range(1, totalV+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

def preorder(node): # 1을 집어넣음
    global cnt
    if node != 0: # node 값이 0이 아니면 들어간다.
        cnt += 1 # 1
        preorder(tree[node][0]) # 1의 left
        preorder(tree[node][1]) # 1의 right

def parent(V1):
    s = []
    while tree[V1][2] != 0:
        s.append(tree[V1][2])
        V1 = tree[V1][2]
    return s

tc = int(input())
for T in range(tc):
    cnt = 0
    totalV, totalE, V1, V2 = map(int, input().split())
    E = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(totalV + 1)]
    # node, left, right
    for i in range(totalE):
        n1 = E[i * 2]  # 부모
        n2 = E[i * 2 + 1]  # 자식
        if tree[n1][0] == 0:
            tree[n1][0] = n2
        else:
            tree[n1][1] = n2
        tree[n2][2] = n1 # 부모표시
    # printTree()
    s1 = parent(V1)
    s2 = parent(V2)
    for i in s1:
        if i in s2:
            preorder(i)
            print("%s%d %d %d" % ('#', T+1, i, cnt)) # 가까운 조상
            break
    # tree를 만들고 그 후 찾고자 하는 정점의 parent 정점을 각각stack에 넣는다.
    # 둘 중 하나의 스택에서 다른쪽스택에 들어있는 수를 발견하자마자 출력한게
    # 가장 가까운 조상이다.