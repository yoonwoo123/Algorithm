import sys
sys.stdin = open("TwoDots.txt")

def DFS(x, y):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if table[nx][ny] == table[x][y]:
            if visited[nx][ny] != 0 and visited[x][y] - visited[nx][ny] > 1:
                return 1

            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1

                if DFS(nx, ny):
                    return 1

    return 0

def search():
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0:
                visited[x][y] = 1
                if DFS(x, y):
                    return 'Yes'

    return 'No'

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

print(search())