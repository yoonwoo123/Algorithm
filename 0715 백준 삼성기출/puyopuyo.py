import sys, collections
sys.stdin = open("puyo_input.txt")

def BFS(x, y, col):
    q = [[x, y]]
    cnt = 1
    chk = [[x, y]]
    visit = [[0 for _ in range(6)] for __ in range(12)]
    visit[x][y] = 1 # 방문체크
    while q:
        x, y = q.pop(0)
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6: continue
            if table[nx][ny] == col and visit[nx][ny] == 0:
                cnt += 1
                visit[nx][ny] = 1
                chk.append([nx, ny])
                q.append([nx, ny])
    if cnt >= 4:
        for i in chk:
            table[i[0]][i[1]] = '.' # 터트려준다
        return 1
    return 0

def down():
    for y in range(6):
        tmp = []
        for x in range(11, -1, -1):
            if table[x][y] == '.': continue
            else:
                tmp.append(table[x][y])
                table[x][y] = '.'
        for i in range(len(tmp)):
            table[11-i][y] = tmp[i]


dx = [0, 0, -1]
dy = [-1, 1, 0]
table = [list(input()) for _ in range(12)]

# for g in table:
#     print(g)
# print()
tot = 0
while True:
    flag = 0
    for x in range(11, -1, -1):
        for y in range(6):
            if table[x][y] != '.':
                if BFS(x, y, table[x][y]): flag = 1
    if flag:
        tot += 1
        down()
    else:
        break
print(tot)