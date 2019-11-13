import sys
sys.stdin = open("카카오1_input.txt")

N = int(input()) # 임의 설정
board = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

answer = 0
s = [] # stack
L = len(board[0]) # N의 크기
for move in moves:
    y = move-1 #내려갈 열
    for x in range(L):
        if board[x][y]:
            if s != [] and s[-1] == board[x][y]:
                s.pop()
                answer += 2
            else:
                s.append(board[x][y])
            board[x][y] = 0
            break
print(answer)