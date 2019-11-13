import sys, itertools
sys.stdin = open("행성연결_input.txt")

def mst():
    tot = 0
    u = 0 # 어디서 시작해도 상관 x
    D[u] = 0 # 선택한 노드의 가중치 0으로

    for _ in range(V):
        min = 9999999999
        for v in range(V):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        if min == 9999999999: break

        visit[u] = 1 # 방문체크
        # for g in arr:
        #     print(g)

        # print(PI[u], u)
        tot += arr[PI[u]][u]
        # print('tot', tot)
        # print()
        for v in range(V):
            if arr[u][v] != 0 and visit[v] == 0 and D[v] > arr[u][v]:
                D[v] = arr[u][v]
                PI[v] = u

    return tot


V = int(input())
arr = [list(map(int, input().split())) for _ in range(V)]

D = [9999999999] * V # 가중치 배열
PI = [x for x in range(V)]  # 부모
visit = [0] * V # 방문체크
print(mst())