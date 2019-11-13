import sys
sys.stdin = open("미로탈출로봇중간단계_input.txt")

def miro(table):
    global x_p, y_p
    while True:
        for i in range(4):
            for n in range(N):
                if x_p + dx[dir[i]] > N - 1 or x_p + dx[dir[i]] < 0 or y_p + dy[dir[i]] > N - 1 or y_p + dy[dir[i]] < 0:
                    break

                if table[x_p + dx[dir[i]]][y_p + dy[dir[i]]] == 0:
                    x_p += dx[dir[i]]
                    y_p += dy[dir[i]]
                    table[x_p][y_p] = 9 # 방문은 9 벽은 4로 하자

                if x_p + dx[dir[i]] > N - 1 or x_p + dx[dir[i]] < 0 or y_p + dy[dir[i]] > N - 1 or y_p + dy[dir[i]] < 0:
                    break

                if table[x_p + dx[dir[i]]][y_p + dy[dir[i]]] == 1:
                    break
                if table[x_p + dx[dir[i]]][y_p + dy[dir[i]]] == 9:
                    return table
        # table[x_p + dx[dir[i]][y_p + dy[dir[i]]]


N = int(input())
table = []
dx = [0, 1, 0, -1, 0] # 공백 1아래 2왼 3위 4오
dy = [0, 0, -1, 0, 1]
# 테이블을 만들때 애초에 더크게만들어서 벽을치자
for i in range(N):
    line = list(map(int, list(input())))
    table.append(line)

dir = list(map(int, list(input().split())))
# dx[dir[0]]  는 아래
# dy[dir[0]]
x_p = 0
y_p = 0
table[0][0] = 9

res = 0
miro(table)
for x in range(N):
    for y in range(N):
        if table[x][y] == 9:
            res += 1
print(res - 1)
# for i in range(N):
#     print(table[i])