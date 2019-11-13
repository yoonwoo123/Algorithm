import sys, collections
sys.stdin = open("불_input.txt")
input = sys.stdin.readline
def BFS(x, y):
    global res, flag
    q = collections.deque()
    for i in range(len(fires)):
        q.append((fires[i][0], fires[i][1], 0, 0))
    q.append([x, y, 1, 0])
    # table[x][y] = '#' # 방문체크
    while q:
        x, y, human, time = q.popleft()
        if res <= time + 1: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                if not human: continue
                if res > time + 1:
                    res = time + 1
                    flag = 1
                return
            if table[nx][ny] == '#' or table[nx][ny] == '*': continue
            if human:
                if time + 2 >= res:continue

                q.append([nx, ny, 1, time + 1])
                table[nx][ny] = '@'
                table[x][y] = '#' # 벽으로할지 고민
            else:
                q.append([nx, ny, 0, time + 1])
                table[nx][ny] = '*'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())
for T in range(1, tc+1):
    Y, X = map(int, input().split())
    table = []
    fires = []
    res = 999999999
    flag = 0
    for x in range(X):
        table.append(list(input()))
        # table[x].pop(-1)
        for y in range(Y):
            if table[x][y] == '@':
                sx, sy = x, y
            elif table[x][y] == '*':
                fires.append([x, y])
    # for g in table:
    #     print(g)
    # print()
    # 불을 먼저 다 옮겨논 후에 상근이 위치를 옮기자.
    BFS(sx, sy)
    # for g in table:
    #     print(g)
    # print()

    if flag:
        print(res)
    else:
        print('IMPOSSIBLE')
from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())
    a = [list(input().strip()) for _ in range(h)]
    dist = [[0]*w for _ in range(h)]
    q = deque()
    sx, sy = 0, 0
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    def bfs():
        q.append((sx, sy, 0))
        dist[sx][sy] = 1
        while q:
            x, y, f = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    if f is 1:
                        continue
                    print(dist[x][y])
                    return
                if dist[nx][ny] or a[nx][ny] == '#':
                    continue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny, f))
        print("IMPOSSIBLE")

    for i in range(h):
        for j in range(w):
            if a[i][j] == '*':
                q.append((i, j, 1))
                dist[i][j] = 1
            elif a[i][j] == '@':
                sx, sy = i, j
                a[i][j] = '.'
            else:
                dist[i][j] = 0

    bfs()