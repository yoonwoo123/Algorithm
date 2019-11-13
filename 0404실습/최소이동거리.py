import sys
sys.stdin = open('최소이동거리_input.txt')

# s: 시작 정점, A: 인접 행렬, D: 거리
# v: 정점 집합, U: 선택된 정점 집합 ( visited )

def getMinIdx():
    minV = 999999  #
    minIdx = 0
    for i in range(N + 1):  # 방문 안 한 노드 중 D가 최소인 노드 찾기
        if visit[i] == 0 and D[i] < minV:
            minIdx = i
            minV = D[i]
    return minIdx

def Dijkstra(N):

    for i in range(N+1):
        if A[0][i]: # 출발점과 인접한 노드
            D[i] = A[0][i] # 가중치 초기화
    visit[0] = 1 # 시작노드 방문처리
    while True:
        node = getMinIdx()
        visit[node] = 1 # D가 가장 작은 노드 방문처리
        if node == N:
            return D[N]

        for x in range(N+1):
            if A[node][x]:  # minIdx에 인접인 노드에 대해
                if D[x] > (D[node] + A[node][x]):     # minIdx를 경유하는 비용이 더 작으면
                    D[x] = D[node] + A[node][x]       # D[x] 갱신

tc = int(input())
for T in range(1, tc+1):
    N, E = map(int, input().split())
    A = [[0 for _ in range(N+1)] for _ in range(N+1)]
    D = [99999999999999] * (N+1) # 0번 부터의 거리(가중치)
    visit = [0] * (N+1) # 방문
    D[0] = 0 # 출발점의 가중치는 0으로
    for i in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w # 방향성 있음
    print('#{} {}'.format(T, Dijkstra(N)))

# 강사님 코드

#
# def dijkstra(goal):
#     D[0] = 0  # 출발점의 가중치
#
#     for i in range(N+1):
#         if arr[0][i]: # 출발점과 인접한 노드
#             D[i] = arr[0][i] # D 초기화
#             visit[0] = 1 # 시작노드
#
#     while True:
#         node= getMinIdx():
