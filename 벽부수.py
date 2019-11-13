from sys import stdin
stdin = open("벽부수고이동_input.txt")
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for g in dist:
    print(g)
print()

def bfs():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y][w]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny][w]:
                continue
            if a[nx][ny] == '0':
                dist[nx][ny][w] = dist[x][y][w] + 1
                q.append((nx, ny, w))
            if a[nx][ny] == '1' and w == 0:
                dist[nx][ny][1] = dist[x][y][w] + 1
                q.append((nx, ny, 1))
    return -1

print(bfs())