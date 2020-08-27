import sys, heapq
sys.stdin = open("최단경로_input.txt")
input = sys.stdin.readline
P = sys.stdout.write

def dijkstra(graph, start):

    INF = float('inf')
    distances = {node : INF for node in graph}
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

    for answer in distances.values():
        print(answer if answer < INF else 'INF')

V, E = map(int, input().split())
start = int(input())

graph = {i : {} for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u] and graph[u][v] <= w: continue
    graph[u][v] = w

dijkstra(graph, start)
