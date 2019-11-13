import sys, itertools
sys.stdin = open("최소신장트리_input.txt")

def mst():
    tot = 0
    u = 0 # 시작번호 아무거나 줘도 됨
    D[u] = 0 # 시작번호 가중치를 0 으로 초기화

    for i in range(V+1): # 가중치 최소값 찾기
        min = 9999999999
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]: # 방문안했으면서 제일 작은놈 찾기
                min = D[v]
                u = v

        visit[u] = 1 # 방문처리
        tot += arr[PI[u]][u]

        for v in range(V+1):
            if arr[u][v] != 0 and visit[v] == 0 and arr[u][v] < D[v]:
                D[v] = arr[u][v] # 가중치 업데이트
                PI[v] = u
    return tot


tc = int(input())
for T in range(1, tc+1):
    V, E = map(int, input().split())

    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = arr[n2][n1] = w

    # for g in arr:
    #     print(g)
    # print()

    D = [9999999999]*(V+1) # 가중치는 무한대
    PI = list(range(V+1))
    visit = [0] * (V+1)

    print('#%d %d' % (T, mst()))

