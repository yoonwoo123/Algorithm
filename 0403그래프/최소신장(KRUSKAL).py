import sys, itertools
sys.stdin = open("최소신장트리_input.txt")



def makeset(x):
    p[x] = x

def findset(x):
    if x == p[x]: return x
    else: return findset(p[x])

def union(x, y):
    p[findset(y)] = findset(x)

def mst_KRUSKAL():
    global V
    cnt = 0 # 간선갯수
    tot = 0 # 가중치의 합
    i = 0   # 제어변수
    while cnt < V: # V 개의 간선을 선택
        p1 = findset(arr[i][0]) # arr[i][0]의 부모를 찾아가라
        p2 = findset(arr[i][1]) # arr[i][1]의 부모를 찾아가라
        if p1 != p2: # 부모가 같지 않다면 사이클이 생기지 않는다는 뜻
            tot += arr[i][2]
            cnt += 1
            p[p2] = p1 # union 역할 p1의 부모는 p2로 바꿔줌 즉 사이클이 생기나 안생기나 알수있게 부모를 하나로 통일
        i += 1
    return tot


tc = int(input())
for T in range(1, tc+1):
    V, E = map(int, input().split())

    arr = [[0 for _ in range(3)] for _ in range(E)]

    p = list(range(V+1)) # makeset

    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr[i][0] = n1
        arr[i][1] = n2
        arr[i][2] = w

    arr.sort(key = lambda x:x[2])

    print('#%d %d' % (T, mst_KRUSKAL()))