import sys, collections, copy
sys.stdin = open("로봇청소_input.txt")
# 0은 청소안한데, 1은 벽, 청소한곳 2

def BFS():
    global res
    q = []
    q.append([rx, ry, dir, 0]) # 현재 방향을 넣고
                             # 현재 방향 기준 왼쪽을 봐야한다
                             # 전부 청소되있거나 벽인경우 바라본방향유지
    leftcnt = 0
    while q:
        x, y, d, cnt = q.pop(0)
        # for g in table:
        #     print(g)
        # print(cnt)
        # print()
        if leftcnt == 4:
            nd = back[d]
            nx, ny = x + dx[nd], y + dy[nd] # 1칸 후진
            if nx < 0 or ny < 0 or nx >= N or ny >= M or table[nx][ny] == 1:
                res = cnt
                return # 작동 멈춤
            q.append([nx, ny, d, cnt])
            leftcnt = 0
            continue

        if table[x][y] == 0:
            table[x][y] = 2 # 청소함
            cnt += 1

        nd = left[d] # 왼쪽방향
        nx, ny = x + dx[nd], y + dy[nd] # nx,ny는 왼쪽으로한칸간상태
        if nx < 0 or ny < 0 or nx >= N or ny >= M or table[nx][ny] == 1 or table[nx][ny] == 2:
            q.append([x, y, nd, cnt])
            leftcnt += 1
            continue

        else:
            q.append([nx, ny, nd, cnt])
            leftcnt = 0


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

left = [3, 0, 1, 2] # left[d] 는 현재방향의 왼쪽
back = [2, 3, 0, 1] # 후진

res = 0
N, M = map(int, input().split())
rx, ry, dir = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
BFS()
print(res)