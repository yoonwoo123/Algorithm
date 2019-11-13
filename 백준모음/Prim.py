V = 4
adj_list =[[] for v in range (V+1)]
visited = [False for _ in range(V+1)]

def addEdge(u, v, w):
    adj_list[u].append((w, v))
    adj_list[v].append((w, u))


def prim(s):
    import heapq
    pq = []
    for adj_v in adj_list[s]:
        heapq.heappush(pq, adj_v)
    visited[s] = True
    answer = 0
    while pq:
        w, v = heapq.heappop(pq)
        if visited[v]:
            continue
        for adj_v in adj_list[v]:
            heapq.heappush(pq, adj_v)
        visited[v] = True
        answer += w

    return answer