import sys
sys.stdin = open("탈출_input.txt")

input = sys.stdin.readline
def BFS():
    while q:
        x, y, w = q.pop(0)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if map[nx][ny] == 'D':
                if w: continue
                return dist[x][y]
            if dist[nx][ny] or map[nx][ny] == 'X': continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny, w))
    return "KAKTUS"

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]
q = []
dist = [[0] * C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if map[x][y] == 'S':
            sx, sy = x, y
            dist[x][y] = 1
        if map[x][y] == '*':
            q.append((x, y, 1))
            dist[x][y] = 1
q.append((sx, sy, 0))
print(BFS())