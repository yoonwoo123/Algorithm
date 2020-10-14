import sys
sys.stdin = open("어른상어_input.txt")

# 1 2 3 4 위 아래 왼 오
# time이 1000이 넘어도 다른 상어가 있다면 -1 출력

dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)

N, M, K = map(int, input().split())
# 상어번호, 냄새
table = [[[0, 0] for _ in range(N)] for _ in range(N)]

sharkPos = {x : [] for x in range(1, M+1)} # x, y, dir
sharkSmell = set() # x, y
sharkDirOrder = {x : [] for x in range(1, M+1)} # 각 방향에 따른 dir 우선순위들

for x in range(N):
    line = list(map(int, input().split()))
    for y in range(N):
        if line[y]:
            table[x][y] = [line[y], K]
            sharkPos[line[y]] = [x, y]
            sharkSmell.add((x, y))
            # table[x][y]의 K가 0이 되면 sharkSmell을 pop 해주자.

sharkDirs = list(map(int, input().split()))
for i in range(1, M+1):
    sharkPos[i].append(sharkDirs[i-1])

for i in range(M):
    tmp = [[]]
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    sharkDirOrder[i+1] = tmp

time = 0
while len(sharkPos) != 1 and time < 1001:
    dieShark = []
    for shark, pos in sharkPos.items():
        x, y, dir = pos
        dirOrder = sharkDirOrder[shark][dir]

        case = 1
        mySmell = 0
        for toDir in dirOrder:
            nx, ny = x + dx[toDir], y + dy[toDir]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            if table[nx][ny][1] == 0:
                if table[nx][ny][0] > 0:
                    dieShark.append(shark)
                else:
                    table[nx][ny][0] = shark
                    sharkPos[shark] = [nx, ny, toDir]
                # 모든 상어가 움직이고 나서 자기 자리에 smell 업뎃
                case = 0
                break

            elif table[nx][ny][0] == shark and mySmell == 0:
                mySmell = toDir

        if case:
            nx, ny = x + dx[mySmell], y + dy[mySmell]
            sharkPos[shark] = [nx, ny, mySmell]

    for shark in dieShark:
        sharkPos.pop(shark)

    delSmell = set()
    for x, y in sharkSmell:
        table[x][y][1] -= 1
        if table[x][y][1] == 0:
            table[x][y][0] = 0
            delSmell.add((x, y))

    for pos in delSmell:
        sharkSmell.remove(pos)

    for shark, pos in sharkPos.items():
        x, y, dir = pos
        sharkSmell.add((x, y))
        table[x][y] = [shark, K]

    time += 1

if time == 1001:
    print(-1)
else:
    print(time)