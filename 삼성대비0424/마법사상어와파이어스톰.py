import sys, collections
sys.stdin = open("마법사2_input.txt")

def rotate(arr):
    newArr = [[0 for _ in range(len(arr))] for w in range(len(arr))]
    for x in range(len(arr)):
        for y in range(len(arr)):
            newArr[y][len(arr) - 1 - x] = arr[x][y]

    return newArr

def check4(x, y):
    iceCnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= len(table) or ny < 0 or ny >= len(table) or table[nx][ny] == 0: continue
        iceCnt += 1
    if iceCnt < 3: return 1
    return 0

def BFS(x, y):
    tot = 0
    q = collections.deque()
    q.append((x, y))
    tot += 1
    table[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(table) or ny < 0 or ny >= len(table) or table[nx][ny] == 0: continue
            q.append((nx, ny))
            tot += 1
            table[nx][ny] = 0

    return tot

N, Q = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(2 ** N)]
levels = list(map(int, input().split()))
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
tot = 0
myMax = 0

for level in levels:
    power = 2 ** level

    for x in range(0, len(table), power):
        for y in range(0, len(table), power):
            board = [[0 for _ in range(power)] for w in range(power)]
            for i in range(x, x + power):
                for j in range(y, y + power):
                    board[i - x][j - y] = table[i][j]

            nBoard = rotate(board)
            for i in range(x, x + power):
                for j in range(y, y + power):
                    table[i][j] = nBoard[i - x][j - y]

    meltPoses = []
    for x in range(len(table)):
        for y in range(len(table)):
            if table[x][y] and check4(x, y):
                meltPoses.append((x, y))

    for posX, posY in meltPoses:
        table[posX][posY] -= 1

for x in range(len(table)):
    for y in range(len(table)):
        if table[x][y]:
            tot += table[x][y]

for x in range(len(table)):
    for y in range(len(table)):
        if table[x][y]:
            myMax = max(myMax, BFS(x, y))

print(tot)
print(myMax)