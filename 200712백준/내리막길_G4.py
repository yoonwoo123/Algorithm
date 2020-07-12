import sys, collections
sys.stdin = open("내리막길_input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dp(x, y):
    if x == M-1 and y == N-1:
        return 1
    if DP[x][y] == -1:
        DP[x][y] = 0

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= M or ny >= N: continue
            if table[x][y] > table[nx][ny]:
                DP[x][y] += dp(nx, ny)
    return DP[x][y]

M, N = map(int, input().split()) # M 행, N 열
table = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1 for _ in range(N)] for q in range(M)]

print(dp(0, 0))