import sys
sys.stdin = open("최소스패닝트리_input.txt")
input = sys.stdin.readline

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(nodeA, nodeB):
    root1 = find(nodeA)
    root2 = find(nodeB)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def makeSet(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    # mst = []
    totWeight = 0

    # 1. 초기화
    for node in graph['nodes']:
        makeSet(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, nodeA, nodeB = edge
        if find(nodeA) != find(nodeB):
            union(nodeA, nodeB)
            # mst.append(edge)
            totWeight += weight

    return totWeight

V, E = map(int, input().split())
parent = {}
rank = {}
graph = {'nodes': set(), 'edges': []}

for _ in range(E):
    nodeA, nodeB, weight = map(int, input().split())
    graph['nodes'].add(nodeA)
    graph['nodes'].add(nodeB)
    graph['edges'].append((weight, nodeA, nodeB))

print(kruskal(graph))

# https://www.fun-coding.org/Chapter20-kruskal-live.html
