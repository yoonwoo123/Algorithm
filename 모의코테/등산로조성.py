import sys, copy, time, collections
sys.stdin = open("등산로_input.txt")

def BFS(x, y):
    global res, sx, sy
    q = collections.deque()
    q.append([x, y, 1])
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if table[nx][ny] >= table[x][y]: continue
            else:
                q.append([nx, ny, cnt + 1])
    if res < cnt:
        res = cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())
for T in range(1, tc+1):
    N, K = map(int, input().split())
    table = []
    mmax = -1
    res = -1

    for x in range(N):
        table.append(list(map(int, input().split())))
        t = max(table[x])
        if t > mmax:
            mmax = t
    highs = []
    for x in range(N):
        for y in range(N):
            if table[x][y] == mmax:
                highs.append([x, y])
    HN = len(highs)
    for i in range(HN): # 최대 5개
        for x in range(N): # 최대 8개
            for y in range(N): # 최대 8
                if x == highs[i][0] and y == highs[i][1]: continue
                for k in range(1, K+1): # 최대 5
                    mymax = -1
                    for q in range(4):
                        nx, ny = x + dx[q], y + dy[q]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                        if table[nx][ny] > mymax:
                            mymax = table[nx][ny]
                    if table[x][y] - k < mymax:
                        if table[x][y] - k < 0: continue
                        sx, sy = highs[i][0], highs[i][1]
                        table[x][y] -= k # 깎아줌
                        BFS(sx, sy)
                        table[x][y] += k # 복구
    print(f'#{T} {res}')