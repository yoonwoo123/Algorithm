# 최소신장트리 알고리즘을 사용해서 풀어보자.
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    global answer
    def DFS(x, tot, visited):
        global answer

        if sum(visited) == n:
            answer = min(answer, tot)
            return

        for y in range(n):
            if table[x][y] and visited[y] == 0:
                visited[y] = 1
                DFS(y, tot + table[x][y], visited)
                visited[y] = 0

    answer = 99999999
    table = [[0 for _ in range(n)] for q in range(n)]
    for a, b, val in costs:
        table[a][b] = table[b][a] = val

    visited = [0 for _ in range(n)]
    for x in range(n):
        visited[x] = 1
        DFS(x, 0, visited)
        visited[x] = 0
    return answer

print(solution(n, costs))