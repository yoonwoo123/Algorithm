import sys, heapq
sys.stdin = open("특정한최단경로_input.txt")
input = sys.stdin.readline

def dijkstra(graph, start):

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

    return distances


def AtoB(graph, mustA, mustB):
    toA = dijkstra(graph, 1)
    toB = dijkstra(graph, mustA)
    toN = dijkstra(graph, mustB)

    if mustA not in toA or mustB not in toB or N not in toN:
        return -1
    else:
        tot = toA[mustA] + toB[mustB] + toN[N]
        return (tot if tot < float('inf') else -1)

def BtoA(graph, mustA, mustB):
    toB = dijkstra(graph, 1)
    toA = dijkstra(graph, mustB)
    toN = dijkstra(graph, mustA)

    if mustA not in toA or mustB not in toB or N not in toN:
        return -1
    else:
        tot = toA[mustA] + toB[mustB] + toN[N]
        return (tot if tot < float('inf') else -1)

N, E = map(int, input().split())
graph = {i : {} for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    if b in graph[a] and c >= graph[a][b]: continue
    graph[a][b] = c
    graph[b][a] = c

mustA, mustB = map(int, input().split())
result1 = AtoB(graph, mustA, mustB)
result2 = BtoA(graph, mustA, mustB)

if result1 == -1 and result2 == -1:
    print(-1)
elif result1 >= 0 and result2 >= 0:
    print(min(result1, result2))
else:
    print(max(result1, result2))