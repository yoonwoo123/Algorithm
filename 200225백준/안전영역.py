import sys, itertools
sys.stdin = open("안전영역_input.txt")
input = sys.stdin.readline

def BFS(h, x, y):
    global ans
    q = [(x, y)]
    table[x][y] = 0
    while q:
        x, y = q.pop(0)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] <= h: continue
            table[nx][ny] = 0
            q.append((nx, ny))

# 가장낮은 높이 ~ 가장 높은 높이 - 1 까지 범위만 체크하면 된다.
ans = 1 # 최대 개수 구하기
N = int(input())
table = []
h_max = -1
h_min = 100
for x in range(N):
    table.append(list(map(int, input().strip().split())))
    h_max = max(h_max, max(table[x]))
    h_min = min(h_min, min(table[x]))

oritable = [[0 for y in range(N)] for x in range(N)]
for x in range(N):
    for y in range(N):
        oritable[x][y] = table[x][y]

for h_rain in range(h_min, h_max):
    cnt = 0
    for x in range(N):
        for y in range(N):
            if table[x][y] > h_rain:
                cnt += 1
                BFS(h_rain, x, y)
    ans = max(ans, cnt)
    for x in range(N):
        for y in range(N):
            table[x][y] = oritable[x][y]
print(ans)