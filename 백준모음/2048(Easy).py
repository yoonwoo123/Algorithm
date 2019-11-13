import sys, copy
sys.stdin = open("2048_input.txt")

def DFS(dep):
    global res, table

    for g in table:
        print(g)
    print()
    if dep == 5:
        for x in range(N):
            for y in range(N):
                if res < table[x][y]:
                    res = table[x][y]
        return

    for i in range(4):
        # 맵 복사
        ori = copy.deepcopy(table)

        if i == 0:
            up()
        elif i == 1:
            down()
        elif i == 2:
            left()
        elif i == 3:
            right()

        DFS(dep + 1)
        # 맵 초기화
        # for x in range(N):
        #     for y in range(N):
        #         table[x][y] = ori[x][y]
        table = copy.deepcopy(ori)

def up():
    for x in range(N):
        for y in range(N):
            if table[x][y] > 0:
                val = table[x][y]
                sx, sy = x, y

                while True:
                    nx, ny = x - 1, y # 상
                    if nx < 0: break
                    if table[nx][ny] > 0: # 숫자만나면
                        if table[nx][ny] == val:
                            if table[x][y] == -1:
                                table[x][y] = val
                                table[sx][sy] = 0

                            else: # 값을 합침 즉 두배로
                                table[nx][ny] *= 2
                                table[x][y] = -1 # 합친값은 또 못합쳐지므로 안전장치
                                table[sx][sy] = 0

                        else:
                            table[x][y] = val
                        break
                    else: # 0 또는 -1 만나면
                        x, y = nx, ny # 현재 좌표를 움직인 좌표로 옮겨줌
            elif table[x][y] == -1:
                table[x][y] = 0 # 쓸모없는 안전장치 제거


def down():
    for x in range(N-1, -1, -1):
        for y in range(N-1, -1, -1):
            if table[x][y] > 0:
                val = table[x][y]
                sx, sy = x, y
                while True:
                    nx, ny = x + 1, y  # 하
                    if nx >= N: break
                    if table[nx][ny] > 0:  # 숫자만나면
                        if table[nx][ny] == val:
                            if table[x][y] == -1:
                                table[x][y] = val
                                table[sx][sy] = 0

                            else:  # 값을 합침 즉 두배로
                                table[nx][ny] *= 2
                                table[x][y] = -1  # 합친값은 또 못합쳐지므로 안전장치
                                table[sx][sy] = 0

                        else:
                            table[x][y] = val
                        break
                    else:  # 0 또는 -1 만나면
                        x, y = nx, ny  # 현재 좌표를 움직인 좌표로 옮겨줌
            elif table[x][y] == -1:
                table[x][y] = 0  # 쓸모없는 안전장치 제거


def left():
    for y in range(N):
        for x in range(N):
            if table[x][y] > 0:
                val = table[x][y]
                sx, sy = x, y
                while True:
                    nx, ny = x, y - 1 # 좌
                    if ny < 0: break
                    if table[nx][ny] > 0:  # 숫자만나면
                        if table[nx][ny] == val:
                            if table[x][y] == -1:
                                table[x][y] = val
                                table[sx][sy] = 0

                            else:  # 값을 합침 즉 두배로
                                table[nx][ny] *= 2
                                table[x][y] = -1  # 합친값은 또 못합쳐지므로 안전장치
                                table[sx][sy] = 0

                        else:
                            table[x][y] = val
                        break

                    else:  # 0 또는 -1 만나면
                        x, y = nx, ny  # 현재 좌표를 움직인 좌표로 옮겨줌
            elif table[x][y] == -1:
                table[x][y] = 0  # 쓸모없는 안전장치 제거

def right():
    for y in range(N-1, -1, -1):
        for x in range(N-1, -1, -1):
            if table[x][y] > 0:
                val = table[x][y]
                sx, sy = x, y
                while True:
                    nx, ny = x, y + 1 # 우
                    if ny >= N: break
                    if table[nx][ny] > 0:  # 숫자만나면
                        if table[nx][ny] == val:
                            if table[x][y] == -1:
                                table[x][y] = val
                                table[sx][sy] = 0

                            else:  # 값을 합침 즉 두배로
                                table[nx][ny] *= 2
                                table[x][y] = -1  # 합친값은 또 못합쳐지므로 안전장치
                                table[sx][sy] = 0

                        else:
                            table[x][y] = val
                        break
                    else:  # 0 또는 -1 만나면
                        x, y = nx, ny  # 현재 좌표를 움직인 좌표로 옮겨줌
            elif table[x][y] == -1:
                table[x][y] = 0  # 쓸모없는 안전장치 제거


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
# ori = [[0 for _ in range(N)] for q in range(N)]
res = -1

# print(table)

DFS(0)
print(res)