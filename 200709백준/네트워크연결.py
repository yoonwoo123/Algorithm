import sys
sys.stdin = open("네트워크연결_input.txt")
input = sys.stdin.readline

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(nodeA, nodeB):
    root1 = find(nodeA)
    root2 = find(nodeB)

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
    totWeight = 0

    for node in graph['nodes']:
        makeSet(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, nodeA, nodeB = edge
        if find(nodeA) != find(nodeB):
            union(nodeA, nodeB)
            totWeight += weight

    return totWeight

N = int(input())
M = int(input())
parent = {}
rank = {}
graph = {'nodes': set(), 'edges': []}

for _ in range(M):
    nodeA, nodeB, weight = map(int, input().split())
    graph['nodes'].add(nodeA)
    graph['nodes'].add(nodeB)
    graph['edges'].append((weight, nodeA, nodeB))
    # A와 B는 같을 수 있다. 같으면 weight가 0이지 않을까?

print(kruskal(graph))