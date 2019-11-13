import sys
sys.stdin = open("스도쿠_input.txt")

def main():
    for x in range(9):
        for y in range(9):
            if arr[x][y] == 0:
                DFS(x, y)
    # square()

def DFS(x, y):
    chk = [0] * 9
    xpos = (x // 3) * 3
    ypos = (y // 3) * 3
    for i in range(xpos, xpos + 3):
        for j in range(ypos, ypos + 3):
            if arr[i][j] == 0: continue
            chk[arr[i][j] - 1] = 1
    if sum(chk) == 8:
        for r in range(9):
            if chk[r] == 0:
                arr[x][y] = r + 1
                return
    for i in range(9): # 가로
        if arr[x][i] == 0: continue
        chk[arr[x][i] - 1] = 1
    if sum(chk) == 8:
        for i in range(9):
            if chk[i] == 0:
                arr[x][y] = i + 1 # 하나만 빌때 값을 넣어줌
                return

    # chk = [0] * 9
    for j in range(9): # 세로
        if arr[j][y] == 0: continue
        chk[arr[j][y] - 1] = 1
    if sum(chk) == 8:
        for j in range(9):
            if chk[j] == 0:
                arr[x][y] = j + 1 # 하나만 빌때 값을 넣어줌
                return




# def square():
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             chk = [0] * 9
#             for x in range(i, i + 3):
#                 for y in range(j, j + 3):
#                     if arr[x][y] == 0:
#                         tx = x
#                         ty = y
#                         continue
#                     chk[arr[x][y] - 1] = 1
#             if sum(chk) == 8:
#                 for r in range(9):
#                     if chk[r] == 0:
#                         arr[tx][ty] = r + 1  # 하나만 빌때 값을 넣어줌
#                         break
def check():
    for x in range(9):
        for y in range(9):
            if arr[x][y] == 0:
                return 0
    return 1

arr = [list(map(int, input().split())) for _ in range(9)]
main()

final = check()
while final:
    if final:
        for i in arr:
            # for q in arr[i]:
            print(' '.join(list(map(str, i))))
            # if i != 8:
            #     print()
        break
    else:
        main()