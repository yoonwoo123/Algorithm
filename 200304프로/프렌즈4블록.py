import sys
sys.stdin = open("프렌즈4블록_input.txt")

m, n = map(int, input().split())
board = [input() for _ in range(m)]

answer = 0
board = [list(board[i]) for i in range(m)]

while True:
    # 터트릴 4블록 찾기
    poses = []
    for x in range(m-1):
        for y in range(n-1):
            if '' != board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
                for i in range(2):
                    for j in range(2):
                        poses.append((x+i, y+j))
    if poses == []: break
    # 터트리고 블록 내리기
    for x, y in poses:
        board[x][y] = ''
    for x in range(m-1, 0, -1):
        for y in range(n):
            if board[x][y] == '':
                sx = x
                while True:
                    nx = sx - 1
                    if nx < 0: break
                    if board[nx][y]:
                        board[x][y], board[nx][y] = board[nx][y], board[x][y]
                        break
                    sx = nx
for x in range(m):
    for y in range(n):
        if board[x][y] == '':
            answer += 1
print(answer)