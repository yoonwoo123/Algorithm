import sys
sys.stdin = open("등굣길_input.txt")
# n = x, m = y
N = int(input()) # 제출 시 빼야함

m, n = map(int, input().split())
puddles = [list(map(int, input().split())) for _ in range(N)]

table = [[0] * m for _ in range(n)]
for x, y in puddles:
    table[x-1][y-1] = -1 # 웅덩이를 맵에 표시

table[0][0] = 1 # 시작점
for x in range(n):
    for y in range(m):
        if table[x][y] < 0: continue
        if y + 1 < m and table[x][y+1] >= 0:
            table[x][y+1] += table[x][y]
        if x + 1 < n and table[x+1][y] >= 0:
            table[x+1][y] += table[x][y]
answer = table[n-1][m-1] % 1000000007
print(answer)
