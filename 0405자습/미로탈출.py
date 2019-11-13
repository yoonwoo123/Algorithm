import sys
sys.stdin = open("미로탈출_input.txt")

def BFS():
    global my_min, flag
    que = []
    que.append([sx, sy, 0])
    # arr[sx][sy] = 0 # 방문
    # bomb = 1 # 사용한 폭탄 개수
    # cnt = 0
    while que:
        x, y, cnt = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= X or ny < 0 or ny >= Y: continue
            if arr[nx][ny] == 1: continue

            if arr[nx][ny] == 4:
                # if memo[nx][ny] > memo[x][y] + 1:
                #     memo[nx][ny] = memo[x][y] + 1
                my_min = cnt + 1
                return

            if arr[nx][ny] == 0:
                if memo[nx][ny] > memo[x][y]:
                    memo[nx][ny] = memo[x][y]
                #     memo[nx][ny] = memo[x][y] + 1
                    que.append([nx, ny, cnt + 1])
                # cnt += 1
                # arr[nx][ny] = 9
                continue
            if arr[nx][ny] == 2 and memo[x][y] < 3: # 만약 뚫을 수 있는 벽이라면? 폭탄은 3개까지
                # bomb += 1
                # memo[nx][ny] = bomb + 1
                if memo[nx][ny] > memo[x][y] + 1:
                    memo[nx][ny] = memo[x][y] + 1
                    que.append([nx, ny, cnt+1])
                # arr[nx][ny] = 9
    flag = 1
    return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

X, Y = map(int, input().split())
arr = []
memo = [[9 for _ in range(Y)] for _ in range(X)]
flag = 0
my_min = 999999999999
for i in range(X):
    arr.append(list(map(int, input().split())))

for x in range(X):
    for y in range(Y):
        if arr[x][y] == 3:
            sx, sy = x, y
            break
memo[sx][sy] = 0
BFS()
# print(BFS() + 1)
if flag == 1:
    print(-1)
else:
    print(my_min)