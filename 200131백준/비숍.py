import sys
sys.stdin = open("비숍_input.txt")

def DFSB(x, y, cnt):
    global ansB
    if N*N-(N*x+y-1)+cnt <= ansB: return

    while x < N:
        while y < N:
            if table[x][y] == 1:
                # chk에 대각선 부분 전부 1로
                table[x][y] = 2
                pos = check(x, y)
                DFSB(x, y, cnt + 1) # 다음 열로
                # chk 한 대각선 전부 0으로 초기화
                table[x][y] = 1
                uncheck(pos)
            y += 2
        y = 0 if x%2 else 1
        x += 1
    ansB = max(ansB, cnt)

def DFSW(x, y, cnt):
    global ansW
    if N*N-(N*x+y-1)+cnt <= ansW: return

    while x < N:
        while y < N:
            if table[x][y] == 1:
                # chk에 대각선 부분 전부 1로
                table[x][y] = 2
                pos = check(x, y)
                DFSW(x, y, cnt + 1) # 다음 열로
                # chk 한 대각선 전부 0으로 초기화
                table[x][y] = 1
                uncheck(pos)
            y += 2
        y = 1 if x%2 else 0
        x += 1
    ansW = max(ansW, cnt)

def check(x, y):
    tmp = []
    for dy in (-1, 1):
        nx, ny = x, y
        while True:
            nx, ny = nx + 1, ny + dy
            if 0 <= nx < N and 0 <= ny < N:
                if table[nx][ny] == 1:
                    table[nx][ny] = 0
                    tmp.append([nx, ny])
            else:
                break
    return tmp

def uncheck(pos):
    for x, y in pos:
        table[x][y] = 1

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
ansB = 0
ansW = 0
DFSB(0, 0, 0)
DFSW(0, 1, 0)
print(ansB+ansW)