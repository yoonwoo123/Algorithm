import sys, copy
sys.stdin = open("청소년상어_input.txt")

# 물고기 움직임 구현
def moveFish(table):
    arr = copy.deepcopy(table)

    for fishNum in range(1, 17):
        if fishNum in fishPos:

            x, y = fishPos[fishNum]
            dir = arr[x][y][1]
            tryNum = 0

            while tryNum < 8:
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or arr[nx][ny][0] == -1:
                    dir = turnLeft[dir]
                    tryNum += 1
                    # 방향 전환 후 nx, ny 다시 구해서 반복탐색

                else: # 둘의 위치를 바꿈
                    if arr[nx][ny][0] == 0:
                        fishPos[arr[x][y][0]] = [nx, ny]
                    else:
                        fishPos[arr[x][y][0]], fishPos[arr[nx][ny][0]] = fishPos[arr[nx][ny][0]], fishPos[arr[x][y][0]]

                    arr[x][y][1] = dir
                    arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                    break

    return arr

def DFS(x, y, tot, table):
    global mymax, fishPos

    for move in range(1, 4): # 상어 움직이는 거리
        dir = table[x][y][1]
        nx, ny = x + dx[dir] * move, y + dy[dir] * move

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or table[nx][ny][0] == 0: continue

        oriFishPos = copy.deepcopy(fishPos)
        eatNum = table[nx][ny][0]
        eatenFishPos = fishPos.pop(eatNum)

        table[nx][ny][0] = -1
        table[x][y] = [0, 0]

        DFS(nx, ny, tot + eatNum, moveFish(table))

        fishPos = copy.deepcopy(oriFishPos)

        table[x][y] = [-1, dir]
        table[nx][ny][0] = eatNum

    # 상어가 이동할 칸이 없으면 return
    mymax = max(mymax, tot)

# DFS 백트래킹으로 table 자체가 항상 변하므로 table을 되돌려야 한다.

answer = 0
table = [] # 상어 번호, dir
fishPos = {s : [] for s in range(1, 17)} # 상어 번호에 따른 위치 값들 자주 갱신해야함
dx = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 0, -1, -1, -1, 0, 1, 1, 1)
turnLeft = (0, 2, 3, 4, 5, 6, 7, 8, 1)

for x in range(4):
    line = list(map(int, input().split()))
    tmp = []

    for y in range(0, 8, 2):
        tmp.append([line[y], line[y+1]])
        fishPos[line[y]] = [x, y//2]

    table.append(tmp)

answer += table[0][0][0]
fishPos.pop(table[0][0][0])
# 상어는 -1로 표현
table[0][0][0] = -1
table = moveFish(table)

mymax = -1
DFS(0, 0, 0, table)
print(mymax + answer)