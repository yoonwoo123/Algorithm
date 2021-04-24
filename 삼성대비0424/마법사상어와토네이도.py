import sys
sys.stdin = open("마법사_input.txt")

def tornado(x, y):
    global tot
    dir = 0

    for i in range(1, N+1): # 0, 0에 도달하면 종료
        for _ in range(2):
            for j in range(i):
                nx, ny = x + dx[dir], y + dy[dir]
                sand = table[nx][ny]
                for k, v in movePoses[dir].items():
                    if k == 100:
                        moveSand = table[nx][ny]
                    else:
                        moveSand = int(sand * k / 100)
                    for mx, my in v:
                        rx, ry = nx + mx, ny + my
                        if rx < 0 or rx >= N or ry < 0 or ry >= N:
                            tot += moveSand
                        else:
                            table[rx][ry] += moveSand
                        table[nx][ny] -= moveSand
                x, y = nx, ny
                if x == 0 and y == 0:
                    return

            dir += 1
            dir %= 4


dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

movePoses = [{1 : [[-1, 1], [1, 1]], 7: [[-1, 0], [1, 0]], 2: [[-2, 0], [2, 0]], 10: [[-1, -1], [1, -1]], 5: [[0, -2]], 100: [[0, -1]]}, {1 : [[-1, -1], [-1, 1]], 7: [[0, -1], [0, 1]], 2: [[0, -2], [0, 2]], 10: [[1, -1], [1, 1]], 5: [[2, 0]], 100: [[1, 0]]}, {1 : [[-1, -1], [1, -1]], 7: [[-1, 0], [1, 0]], 2: [[-2, 0], [2, 0]], 10: [[-1, 1], [1, 1]], 5: [[0, 2]], 100: [[0, 1]]}, {1 : [[1, -1], [1, 1]], 7: [[0, -1], [0, 1]], 2: [[0, -2], [0, 2]], 10: [[-1, -1], [-1, 1]], 5: [[-2, 0]], 100: [[-1, 0]]}]

tot = 0
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

x = y = N // 2
tornado(x, y)
print(tot)