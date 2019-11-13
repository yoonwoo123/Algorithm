import sys
sys.stdin = open('최소비용_input.txt')

def BFS(x, y):
    global sol
    que = []
    que.append([x, y])
    while que:
        x, y = que.pop(0)
        for i in range(4):
            term = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if arr[nx][ny] > arr[x][y]:
                term = arr[nx][ny] - arr[x][y]
            if memo[nx][ny] > 1 + memo[x][y] + term:
                memo[nx][ny] = 1 + memo[x][y] + term
                que.append([nx, ny])
    sol = memo[N-1][N-1]

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    arr = []
    sol = 0
    memo = [[9999999999999 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        arr.append(list(map(int, input().split())))
    memo[0][0] = 0
    BFS(0, 0)
    print('#%d %d' % (T, sol))