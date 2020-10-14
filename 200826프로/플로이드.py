import sys
sys.stdin = open("플로이드_input.txt")
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph[1:]:
    for col in row[1:]:
        if col == float('inf'):
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()

# https://claude-u.tistory.com/334