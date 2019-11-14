import sys
sys.stdin = open("게리맨더링2_input.txt")

def START(sx, sy, L, R):
    global flag, scores
    osx, osy = sx, sy # 혹시 몰라 복사
    lx, ly = sx + dx[0] * L, sy + dy[0] * L
    if lx < 0 or ly < 0 or lx >= N or ly >= N: return
    rx, ry = sx + dx[1] * R, sy + dy[1] * R
    if rx < 0 or ry < 0 or rx >= N or ry >= N: return
    fx, fy = sx + dx[0] * L + dx[1] * R, sy + dy[0] * L + dy[1] * R
    if fx < 0 or fy < 0 or fx >= N or fy >= N: return

    olx, oly = lx, ly
    orx, ory = rx, ry
    ofx, ofy = fx, fy

    visit[sx][sy] = 1
    while True:
        nx, ny = sx + dx[0], sy + dy[0]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return
        if nx == lx and ny == ly:
            visit[nx][ny] = 1
            break
        visit[nx][ny] = 1
        sx, sy = nx, ny
    sx, sy = osx, osy
    while True:
        nx, ny = sx + dx[1], sy + dy[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return
        if nx == rx and ny == ry:
            visit[nx][ny] = 1
            break
        visit[nx][ny] = 1
        sx, sy = nx, ny
    sx, sy = osx, osy
    while True:
        nx, ny = lx + dx[1], ly + dy[1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return
        if nx == fx and ny == fy:
            visit[nx][ny] = 1
            break
        visit[nx][ny] = 1
        lx, ly = nx, ny
    lx, ly = olx, oly
    while True:
        nx, ny = rx + dx[0], ry + dy[0]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return
        if nx == fx and ny == fy: break
        visit[nx][ny] = 1
        rx, ry = nx, ny
    rx, ry = orx, ory
    flag = 1
    # 선거구 값을 구해주자

    for x in range(lx):
        for y in range(sy + 1):
            if visit[x][y]: break
            scores[0] += table[x][y]

    for x in range(rx+1):
        for y in range(N-1, sy, -1):
            if visit[x][y]: break
            scores[1] += table[x][y]

    for x in range(lx, N):
        for y in range(fy):
            if visit[x][y]: break
            scores[2] += table[x][y]

    for x in range(rx+1, N):
        for y in range(N-1, fy-1, -1):
            if visit[x][y]: break
            scores[3] += table[x][y]
    scores[4] = tot - scores[0] - scores[1] - scores[2] - scores[3]

dx = [1, 1]
dy = [-1, 1]
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
tot = 0
for x in range(N):
    tot += sum(table[x])

visit = [[0 for _ in range(N)] for q in range(N)]
res = 999999999
# 점은 총 4개로 sx,sy / lx, ly/ rx, ry/ fx, fy
for L in range(1, N//2 + 1):
    for R in range(1, N//2 + 1):
        if N % 2 == 0 and L == N//2 and R == N//2: continue
        for x in range(N-2): # sx가 들어갈 수 있는 공간
            for y in range(1, N-1): # sy 가 될 공간
                flag = 0
                scores = [0] * 5
                START(x, y, L, R)
                if flag:
                    c = max(scores) - min(scores)
                    if res > c:
                        res = c
                    visit = [[0 for _ in range(N)] for q in range(N)]
print(res)