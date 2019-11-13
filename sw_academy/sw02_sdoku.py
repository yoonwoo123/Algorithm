import sys
sys.stdin = open("sw02_sdoku_input.txt")

def sdoku(data):
    for x in range(9):
        blank = []
        for y in range(9):
            if data[x][y] not in blank:
                blank.append(data[x][y])
        if len(blank) != 9:
            return 0
    for x in range(9):
        blank = []
        for y in range(9):
            if data[y][x] not in blank:
                blank.append(data[y][x])
        if len(blank) != 9:
            return 0
    for k in range(3):
        for t in range(3):
            blank = []
            for x in range(3):

                for y in range(3):
                    if data[x + 3*k][y + 3*t] not in blank:
                        blank.append(data[x + 3*k][y + 3*t])
            if len(blank) != 9:
                return 0
    return 1

testcases = input()
for T in range(int(testcases)):
    data = []

    for i in range(9):
        line = list(map(int, input().split()))
        data.append(line)
    #가로 1줄씩 검사, 세로 1줄씩 검사, 격자 9개 검사
    #빈리스트에 넣어서 겹치면 안넣는조건으로 len!=9라면 False

    print(f'#{T+1} {sdoku(data)}')