import sys
sys.stdin = open("최단경로_input.txt")

def mst():
    # tot = 0
    u = U-1 # 시작번호 아무거나 줘도 됨
    D[u] = 0 # 시작번호 가중치를 0 으로 초기화

    for i in range(V): # 가중치 최소값 찾기
        min = 9999999999
        N = -1
        for v in range(V):
            if visit[v] == 0 and min > D[v]: # 방문안했으면서 제일 작은놈 찾기
                min = D[v]
                N = v
        if min == 9999999999: break

        visit[N] = 1 # 방문처리
        # print(arr[PI[u]][u])
        # tot += arr[PI[u]][u]

        for v in range(V):
            if visit[v]: continue
            via = D[N] + arr[N][v]
            if D[v] > via:
                D[v] = via
            # if arr[u][v] != 0 and visit[v] == 0 and arr[u][v] < D[v]:
            #     D[v] = arr[u][v] # 가중치 업데이트
            #     print(arr[u][v])
            #     PI[v] = u
    # print(D)
    return D

V, E = map(int, input().split())
U = int(input())
arr = [[9999999999 for _ in range(V)] for q in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    arr[u-1][v-1] = w
    # arr[v-1][u-1] = w
# for g in arr:
#     print(g)
# print()
# arr = [list(map(int, input().split())) for _ in range(V)]

D = [9999999999]*V # 가중치는 무한대
# PI = list(range(V)) # 부모
visit = [0] * V # 방문

# print(mst())
for d in mst():
    print(d if d != 9999999999 else "INF")