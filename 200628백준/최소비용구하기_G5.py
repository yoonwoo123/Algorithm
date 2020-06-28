# 제목 뒤 G5는 백준 티어 Gold5를 나타냄
import sys, math
sys.setrecursionlimit(10**6)
sys.stdin = open("최소비용구하기_input.txt")

# def DFS(cur, tot):
#     global ans
#
#     if ans <= tot: return # 가지치기
#     if cur == ecity:
#         ans = min(ans, tot)
#         return
#     # 같은 도시로 두 번 갈 필요 없기 때문에 방문체크를 해 주자.
#     # 비용이 0일수 있기 때문에 두 번 이상 가는게 최소일 경우도 있을듯
#     for i in range(N):
#         if table[cur][i] >= 0:
#             DFS(i, tot + table[cur][i])
#
# ans = math.inf
# N = int(input())
# M = int(input())
# table = [[-1 for q in range(N)] for w in range(N)]
# for i in range(M):
#     start, end, cost = map(int, input().split())
#     table[start-1][end-1] = cost
# # print(table)
# scity, ecity = map(int, input().split())
# scity -= 1
# ecity -= 1
# # 출발지점으로부터 시작하는 DFS를 만들어서 최소값 구하므로
# # 계산중 더 커지면 return 하는 가지치기 구현하자.
# # 만약 scity와 ecity가 같다면 답은 0으로 되야한다.
# # 버스이용 비용이 0일 수도 있으므로 맵의 기본값을 -1로 하자
# DFS(scity, 0)
# print(ans)

def mst(u):
    tot = 0
    # u =  # 시작번호 아무거나 줘도 됨
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


V = int(input())
E = int(input())

arr = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    arr[n1][n2] = w

# for g in arr:
#     print(g)
# print()

D = [9999999999]*(V+1) # 가중치는 무한대
PI = list(range(V+1))
visit = [0] * (V+1)
print(D, PI)
scity, ecity = map(int, input().split())
print(mst(scity))

# 출처: https://dojinkimm.github.io/problem_solving/2019/12/09/boj-1916-mincost.html

# import sys
# import heapq
# r = sys.stdin.readline
# INF = 1e9
#
#
# def dijkstra(n, s, e, edg):
#     q = []
#     dist = [INF] * n
#     dist[s-1] = 0
#     heapq.heappush(q, [s-1, 0])
#
#     while q:
#         pos, cost = heapq.heappop(q)
#
#         for p, c in edg[pos]:
#             c += cost
#             if c < dist[p]:
#                 dist[p] = c
#                 heapq.heappush(q, [p, c])
#     return dist[e-1]
#
#
# N = int(r())
# M = int(r())
# edges = [[] for _ in range(N)]
# for i in range(M):
#     u, v, w = list(map(int, r().split()))
#     edges[u-1].append([v-1, w])
#
# st, end = map(int, r().split())
#
# print(dijkstra(N, st, end, edges))