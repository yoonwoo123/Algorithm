# 0628백준 못풀었던 최소비용구하기 재도전

import sys, heapq
sys.stdin = open("최소비용_input.txt")
input = sys.stdin.readline

def dijkstra(graph, start, end):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)

        if currentDistance > distances[currentNode]: continue

        for adjacent, weight in graph[currentNode].items():
            distance = currentDistance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances[end]

N = int(input())
M = int(input())

graph = {i : {} for i in range(1, N+1)}

for _ in range(M):
    start, end, toll = map(int, input().split())
    # 주의해야할 점!! 같은 버스(같은 키)값으로 더 큰 값이 들어오는건 무시해줘야
    # 최소비용을 정확히 구할 수 있다.
    if end in graph[start] and toll >= graph[start][end]: continue
    graph[start][end] = toll

start, end = map(int, input().split())
print(dijkstra(graph, start, end))
