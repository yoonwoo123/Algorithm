import sys
sys.stdin = open("미세먼지_input.txt")

def diff(x, y): # 확산
    ori = table[x][y] # 원래 먼지값
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
        if table[nx][ny] == -1: continue
        tmp[nx][ny] += ori // 5
        tmp[x][y] -= ori // 5


R, C ,T = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

table = []
air = []

for x in range(R):
    table.append(list(map(int, input().split())))
    for y in range(C):
        if len(air) == 2: break
        if table[x][y] == -1:
            air.append([x, y])
            continue

####
for z in range(T):
    tmp = [[0 for _ in range(C)] for q in range(R)]

    for x in range(R): # 전체 확산
        for y in range(C):
            if table[x][y] < 5: continue
            else:
                diff(x, y)
    for x in range(R):
        for y in range(C):
            table[x][y] += tmp[x][y]
    ####
    # for g in table:
    #     print(g)
    # print()

    a1x, a1y = air[0][0], air[0][1]

    dir1x = [-1, 0, 1, 0]
    dir1y = [0, 1, 0, -1]

    d = 0
    while True:
        nax = a1x + dir1x[d]
        nay = a1y + dir1y[d]

        if nax < 0 or nay < 0 or nax >= R or nay >= C or nax > air[0][0]:
            d += 1
            continue
        if table[nax][nay] == -1:
            table[a1x][a1y] = 0
            break

        if table[a1x][a1y] == -1:
            pass
        else:
            table[a1x][a1y] = table[nax][nay]

        a1x = nax
        a1y = nay

    a2x, a2y = air[1][0], air[1][1]

    dir2x = [1, 0, -1, 0]
    dir2y = [0, 1, 0, -1]

    d = 0
    while True:
        nax = a2x + dir2x[d]
        nay = a2y + dir2y[d]

        if nax < 0 or nay < 0 or nax >= R or nay >= C or nax < air[1][0]:
            d += 1
            continue
        if table[nax][nay] == -1:
            table[a2x][a2y] = 0
            break

        if table[a2x][a2y] == -1:
            pass
        else:
            table[a2x][a2y] = table[nax][nay]

        a2x = nax
        a2y = nay
    # for g in table:
    #     print(g)
    # print()
tot = 0
for x in range(R):
    for y in range(C):
        tot += table[x][y]
print(tot + 2)