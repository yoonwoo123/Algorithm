import sys, itertools
sys.stdin = open("행성연결_input.txt")

def mst():
    tot = 0
    u = 0 # 시작번호 아무거나 줘도 됨
    D[u] = 0 # 시작번호 가중치를 0 으로 초기화

    for i in range(V): # 가중치 최소값 찾기
        min = 9999999999
        for v in range(V):
            if visit[v] == 0 and min > D[v]: # 방문안했으면서 제일 작은놈 찾기
                min = D[v]
                u = v
        if min == 9999999999: break

        visit[u] = 1 # 방문처리
        tot += arr[PI[u]][u]

        for v in range(V):
            if arr[u][v] != 0 and visit[v] == 0 and arr[u][v] < D[v]:
                D[v] = arr[u][v] # 가중치 업데이트
                PI[v] = u
    return tot

V = int(input())
arr = [list(map(int, input().split())) for _ in range(V)]

D = [9999999999]*V # 가중치는 무한대
PI = list(range(V)) # 부모
visit = [0] * V # 방문

print(mst())