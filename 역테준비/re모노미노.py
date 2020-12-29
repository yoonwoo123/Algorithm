import sys
sys.stdin = open("모노미노도미노_input.txt")
input = sys.stdin.readline

# 각 열(y)마다 얼만큼 낮은 칸까지 떨어질 수 있나 체크
def dropblock(ny, board):
    nx = 0
    while True:
        if nx == 6 or board[nx][ny]:
            nx -= 1
            break
        nx += 1
    return nx

def dropblock2(nx, ny, board):
    while True:
        nx += 1
        if nx == 6 or board[nx][ny]:
            nx -= 1
            break
    return nx

def scorecheck(board):
    global score
    flag = 0
    for row in range(5, 1, -1):
        count = 0
        for col in range(4):
            if board[row][col]:
                count += 1
        if count == 4:
            score += 1
            for col in range(4):
                board[row][col] = 0
            flag = 1
    if flag:
        down(board)
        scorecheck(board)

def down(board):
    visit = {}
    for row in range(4, -1, -1):
        for col in range(4):
            if (row, col) not in visit and board[row][col]:
                if col < 3 and board[row][col] == board[row][col + 1]:
                    min1 = dropblock2(row, col, board)
                    min2 = dropblock2(row, col + 1, board)
                    min3 = min(min1, min2)
                    if min3 != row:
                        board[min3][col] = board[row][col]
                        board[min3][col + 1] = board[row][col + 1]
                        board[row][col] = board[row][col + 1] = 0
                    visit[(row, col)] = visit[(row, col + 1)] = 1

                else:
                    visit[(row, col)] = 1
                    idx = dropblock2(row, col, board)
                    if idx != row:
                        board[idx][col] = board[row][col]
                        board[row][col] = 0

def cleanboard(board):
    cnt = 0
    for i in range(2):
        for j in range(4):
            if board[i][j]:
                cnt += 1
                break

    for _ in range(cnt):
        for j in range(4):
            for i in range(5, 0, -1):
                board[i][j] = board[i - 1][j]
            board[0][j] = 0

n = int(input())
score = 0

greenboard = [[0] * 4 for _ in range(6)]
blueboard = [[0] * 4 for _ in range(6)]

for time in range(1, n + 1):
    t, x, y = map(int, input().split())

    if t == 1:
        ng = dropblock(y, greenboard)
        greenboard[ng][y] = time
        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time

    elif t == 2:
        ng1 = dropblock(y, greenboard)
        ng2 = dropblock(y + 1, greenboard)
        ng = min(ng1, ng2)
        greenboard[ng][y] = greenboard[ng][y + 1] = time

        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time
        nb = dropblock(x, blueboard)
        blueboard[nb][x] = time


    else:
        nb1 = dropblock(x, blueboard)
        nb2 = dropblock(x + 1, blueboard)
        nb = min(nb1, nb2)
        blueboard[nb][x] = blueboard[nb][x + 1] = time

        ng = dropblock(y, greenboard)
        greenboard[ng][y] = time
        ng = dropblock(y, greenboard)
        greenboard[ng][y] = time

    scorecheck(greenboard)
    cleanboard(greenboard)

    scorecheck(blueboard)
    cleanboard(blueboard)

tot = 0
for i in range(6):
    for j in range(4):
        if greenboard[i][j]:
            tot += 1
        if blueboard[i][j]:
            tot += 1

print(score)
print(tot)