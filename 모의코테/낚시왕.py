import sys
sys.stdin = open("낚시왕_input.txt")

def move(i, x, y, s, d, z):
    # 새 table에 상어를 표시하면서 좌표도 바꾼다.
    for _ in range(s):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 1 or ny < 1 or nx >= R+1 or ny >= C+1:
            if d == 0 or d == 1:
                d = (d + 1) % 2
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            nx, ny = x + dx[d], y + dy[d]
        x, y = nx, ny
    if table[x][y] == 0:
        table[x][y] = z
        shks[i][0] = x
        shks[i][1] = y
        shks[i][3] = d # 샤크의 좌표값과 방향 바꿔줌
    elif table[x][y] != 0:
        if z > table[x][y]: # 몸집이 같은경우 x
            die.append(table[x][y]) # 나중에 없앨 상어의 크기
            table[x][y] = z
            shks[i][0] = x
            shks[i][1] = y
            shks[i][3] = d
        else:
            die.append(z)

R, C, M = map(int, input().split()) # M = 상어의수
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

table = [[0 for _ in range(C+1)] for q in range(R+1)]
shks = []
for i in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    table[r][c] = z
    shks.append([r, c, s, d-1, z])
# r, c, s, d, z 행 열 속도 방향 몸집

# 경계면 조심, 상어는 1~R+1, 1~C+1 까지 분포함

tot = 0
for y in range(1, C+1):
    #### 낚시꾼 이동 및 상어 사냥
    die = []
    kill = 0 # 임의의 값
    for x in range(1, R+1):
        if table[x][y] != 0:
            tot += table[x][y]
            kill = table[x][y]
            die.append(kill)
            table[x][y] = 0 # 상어 잡음
            break
    #####
    slen = len(shks)
    for i in range(slen):
        table[shks[i][0]][shks[i][1]] = 0
    # table = [[0 for _ in range(C + 1)] for q in range(R + 1)]
    # 상어 이동

    for i in range(slen):
        x, y, s, d, z = shks[i]
        if z == kill: continue
        move(i, x, y, s, d, z)
    # 이동한 좌표로 맵에 표시 몸집이 더 크면 작은애 잡음
    # 먹힌 상어 좌표 없앰
    i = 0
    for cnt in range(len(die)):
        while True:
            if shks[i][4] == die[cnt]:
                shks.pop(i)
                i = 0
                break
            else:
                i += 1
print(tot)