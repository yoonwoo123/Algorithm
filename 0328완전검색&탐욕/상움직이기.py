import sys
sys.stdin = open("상움직이기_input.txt")

dx = [-3, -2, 2, 3, 3, 2, -2, -3]
dy = [2, 3, 3, 2, -2, -3, -3, -2]

def BFS(x, y, cnt):
    global res
    que = []
    que.append([x, y, cnt])
    arr[x][y] = 1 # 방문체크
    while que:
        x, y, cnt = que.pop(0)
        # cnt += 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == 1: continue
            if arr[nx][ny] == 2:
                res = cnt
                return
            arr[nx][ny] = 1 # 방문체크
            que.append([nx, ny, cnt+1])

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    SX, SY, EX, EY = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[EX][EY] = 2  # 목표지점
    res = 0
    BFS(SX, SY, 1)
    print('#%d %d' % (T, res))