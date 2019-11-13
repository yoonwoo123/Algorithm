import sys
sys.stdin = open("구슬굴리기_input.txt")

w, h = map(int, input().split())
table = []
dx = [0, -1, 1, 0, 0] # 공백 1위 2아래 3왼 4오
dy = [0, 0, 0, -1, 1]

for i in range(h):
    table.append(list(map(int, input())))

N = int(input())
dir = list(map(int, input().split())) # 방향정보

for x in range(h):
    for y in range(w):
        if table[x][y] == 2:
            x_p = x
            y_p = y
            break
table[x_p][y_p] = 9
for i in range(N):  # 방향주어진 개수만큼
    while True:
        nx = x_p + dx[dir[i]]
        ny = y_p + dy[dir[i]]
        if nx > h - 1 or nx < 0 or ny > w - 1 or ny < 0:
            break

        if table[nx][ny] == 0:
            x_p = nx
            y_p = ny
            table[x_p][y_p] = 9  # 방문은 9 벽은 4로 하자

        elif table[nx][ny] == 1:
            break
        elif table[nx][ny] == 9:
            x_p = nx
            y_p = ny
            continue
res = 0
for x in range(h):
    for y in range(w):
        if table[x][y] == 9:
            res += 1
print(res)