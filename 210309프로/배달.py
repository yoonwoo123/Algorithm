import heapq

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

def solution(N, road, K):
    answer = 0

    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        q = []
        heapq.heappush(q, [distances[start], start])

        while q:
            curDistance, curNode = heapq.heappop(q)

            if distances[curNode] < curDistance: continue

            for adjacent, weight in graph[curNode].items():
                distance = curDistance + weight

                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(q, [distance, adjacent])

        return distances

    graph = {i : {} for i in range(1, N+1)}

    for start, end, weight in road:
        if end in graph[start] and weight >= graph[start][end]: continue
        if start in graph[end] and weight >= graph[end][start]: continue
        graph[start][end] = weight
        graph[end][start] = weight

    distances = dijkstra(graph, 1)

    for distance in distances.values():
        if distance <= K: answer += 1

    return answer


print(solution(N, road, K))