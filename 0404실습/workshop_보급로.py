import sys
sys.stdin = open("보급로_input.txt")

def BFS(x, y):
    que = []
    que.append([x, y])
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            if memo[x][y] + arr[nx][ny] < memo[nx][ny]:
                memo[nx][ny] = memo[x][y] + arr[nx][ny]
                que.append([nx, ny])
tc = int(input())
for T in range(1, tc+1):
    dx = [0, 1, 0, -1] # 우, 하, 좌, 상
    dy = [1, 0, -1, 0]

    N = int(input())
    arr = []
    memo = [[99999999999999 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        arr.append(list(map(int, input())))

    memo[0][0] = arr[0][0]
    BFS(0, 0)
    print('#%d %d' % (T, memo[N-1][N-1]))