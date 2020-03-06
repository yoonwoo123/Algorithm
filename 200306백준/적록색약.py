import sys
sys.stdin = open("적록색약_input.txt")
input = sys.stdin.readline

def BFS(col):
    while q:
        x, y = q.pop(0)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] != col: continue
            table[nx][ny] = ''
            q.append((nx, ny))

def BFS2(col):
    while q:
        x, y = q.pop(0)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] == 'B' or table[nx][ny] == '': continue
            table[nx][ny] = ''
            q.append((nx, ny))

N = int(input())
table = [list(input()) for _ in range(N)]
oritable = [[0 for _ in range(N)] for q in range(N)]
for x in range(N):
    for y in range(N):
        oritable[x][y] = table[x][y]
ans = 0
ans2 = 0
for x in range(N):
    for y in range(N):
        if table[x][y]:
            q = [(x, y)]
            col = table[x][y]
            table[x][y] = ''
            BFS(col)
            ans += 1
for x in range(N):
    for y in range(N):
        table[x][y] = oritable[x][y]
for x in range(N):
    for y in range(N):
        if table[x][y]:
            q = [(x, y)]
            col = table[x][y]
            table[x][y] = ''
            if col == 'B':
                BFS(col)
            else:
                BFS2(col)
            ans2 += 1
print(ans, ans2)