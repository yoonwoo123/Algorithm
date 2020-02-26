import sys
sys.stdin = open("자물쇠와열쇠_input.txt")
input = sys.stdin.readline

def Sol():
    global answer
    for x in range(LT-M+1):
        for y in range(LT-M+1):
            for i in range(x, x + M):
                for j in range(y, y + M):
                    table[i][j] += key[i-x][j-y]
            if check():
                answer = True
                return
            reset()

def check():
    for x in range(M - 1, M - 1 + N):
        for y in range(M - 1, M - 1 + N):
            if table[x][y] == 2 or table[x][y] == 0: return 0
    return 1

def reset():
    for x in range(M - 1, M - 1 + N):
        for y in range(M - 1, M - 1 + N):
            table[x][y] = lock[x - M + 1][y - M + 1]

def rotate(arr):
    tmp = [[0 for x in range(M)] for y in range(M)]
    for x in range(M):
        for y in range(M):
            tmp[y][-1-x] = key[x][y]
    return tmp

key = [[0, 0, 0],[1, 0, 0],[0, 1, 1]]
lock = [[1, 1, 1],[1, 1, 0],[1, 0, 1]]

answer = False
N = len(lock)
M = len(key)

LT = 2*(M-1) + N
table = [[3 for y in range(LT)] for x in range(LT)]
reset()
for _ in range(4):
    Sol()
    if answer: break
    key = rotate(key)

print(answer)
