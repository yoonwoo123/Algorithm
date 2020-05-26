import collections
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

# 최단경로로 가되, 가장 멀리 떨어진 노드들의 개수를 구하는 것

def solution(n, edge):

    def BFS():
        q = collections.deque()
        q.append((1, 0))

        while q:
            node, cnt = q.popleft()
            if fasts[node] == -1:
                fasts[node] = cnt
                for next in nodes[node]:
                    q.append((next, cnt + 1))

    fasts = [-1 for _ in range(n+1)] # 각 노드들의 최단경로길이 갱신하자
    # 그 후 최단경로들 중에서 가장 큰 max값의 개수가 몇개인지 세주면 끝
    nodes = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        nodes[edge[i][0]].append(edge[i][1])
        nodes[edge[i][1]].append(edge[i][0])

    BFS()
    print(fasts)

    return fasts.count(max(fasts))

print(solution(n, edge))

## 단비 코드
import collections

Graph = dict()
visited = []


def bfs(n):
    result = []
    Q = collections.deque()
    Q.append([1, 0])
    visited[1] = 1
    while Q:
        t, cnt = Q.popleft()
        result.append((t, cnt))
        for i in Graph[t]:
            if not visited[i]:
                visited[i] = 1
                Q.append([i, cnt+1])
    return result


def solution(n, edges):
    answer = 0
    for i in range(n+1):
        visited.append(0)
    for edge in edges:
        s, e = edge
        if Graph.get(s):
            Graph[s].append(e)
        else:
            Graph[s] = [e]
        if Graph.get(e):
            Graph[e].append(s)
        else:
            Graph[e] = [s]



    bfs_data = bfs(n)
    Max = bfs_data[-1][1]
    print(bfs_data)
    for i in range(len(bfs_data)-1, -1, -1):
        if bfs_data[i][1] == Max:
            answer += 1
    return answer

print(solution(n, edge))

# def solution(n, edge):
#
#     def DFS(node, cnt):
#         if cnt >= fasts[node]: return
#         for next in nodes[node]:
#             if cnt < fasts[node]:
#                 fasts[node] = cnt
#                 DFS(next, cnt + 1)
#                 fasts[node] = 999999
#         print(node, fasts[node], cnt)
#         fasts[node] = min(fasts[node], cnt)
#
#     fasts = [999999 for _ in range(n+1)] # 각 노드들의 최단경로길이 갱신하자
#     fasts[0] = fasts[1] = -1
#     # 그 후 최단경로들 중에서 가장 큰 max값의 개수가 몇개인지 세주면 끝
#     nodes = {}
#     for i in range(len(edge)):
#         if edge[i][0] not in nodes:
#             nodes[edge[i][0]] = [edge[i][1]]
#         else:
#             nodes[edge[i][0]].append(edge[i][1])
#
#         if edge[i][1] not in nodes:
#             nodes[edge[i][1]] = [edge[i][0]]
#         else:
#             nodes[edge[i][1]].append(edge[i][0])
#
#     print(nodes)
#
#     for i in range(len(nodes[1])):
#         DFS(nodes[1][i], 1)
#
#     return fasts.count(max(fasts))
#
# print(solution(n, edge))
#########################################################
# def solution(n, edge):
#
#     def DFS(node, cnt):
#         if cnt >= fasts[node]: return
#
#         for i in range(len(edge)):
#             if 1 not in edge[i] and node in edge[i]:
#                 if cnt + 1 >= edge[i][(edge[i].index(node) + 1) % 2]: continue
#                 fasts[node] = cnt
#                 # visited[i] = 1
#                 # print(node, edge[i][(edge[i].index(node) + 1) % 2])
#                 DFS(edge[i][(edge[i].index(node) + 1) % 2], cnt + 1)
#                 # visited[i] = 0
#         fasts[node] = min(fasts[node], cnt)
#
#     answer = 0
#     fasts = [999999 for _ in range(n+1)] # 각 노드들의 최단경로길이 갱신하자
#     fasts[0] = fasts[1] = -1
#     # 그 후 최단경로들 중에서 가장 큰 max값의 개수가 몇개인지 세주면 끝
#     visited = [0 for _ in range(len(edge))] # 방문체크
#     edge.sort()
#     # print(edge)
#     for i in range(len(edge)):
#         if edge[i][0] == 1:
#             # visited[i] = 1
#             DFS(edge[i][1], 1)
#             # visited[i] = 0
#         else: break
#     # print(fasts)
#     fasts.sort(reverse=True)
#     cnt = 0
#     for fast in fasts:
#         if fasts[0] != 999999 and fasts[0] == fast:
#             cnt += 1
#         else:
#             break
#     return cnt
#
# print(solution(n, edge))