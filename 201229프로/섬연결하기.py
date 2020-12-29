
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):

    def find(node):
        # path compression 기법
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_v, node_u):
        root1 = find(node_v)
        root2 = find(node_u)

        # union-by-rank 기법
        if rank[root1] > rank[root2]:
            parent[root2] = root1

        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    def make_set(node):
        parent[node] = node
        rank[node] = 0

    def kruskal(graph):
        mst = []

        # 1. 초기화
        for node in graph['vertices']:
            make_set(node)

        # 2. 간선 weight 기반 sorting
        edges = graph['edges']
        edges.sort(key= lambda x:x[2])

        # 3. 간선 연결 (사이클 없는)
        for edge in edges:
            node_v, node_u, weight = edge
            if find(node_v) != find(node_u):
                union(node_v, node_u)
                mst.append(edge)

        return mst

    parent = {}
    rank = {}

    mygraph = {}
    mygraph['vertices'] = [x for x in range(n)]
    mygraph['edges'] = costs

    mst = kruskal(mygraph)
    answer = 0
    for node_v, node_u, weight in mst:
        answer += weight

    return answer

print(solution(n, costs))