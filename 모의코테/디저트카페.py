import sys, collections
sys.stdin = open("디저트카페_input.txt")

def Search(x, y, i, j):
    global flag, mymax, flag2
    sx, sy = x, y
    for a in range(i):
        nx, ny = x + dx[0], y + dy[0]
        if nx >= N or ny >= N:
            flag2 = 1
            return
        if chk[table[nx][ny]] == 0:
            chk[table[nx][ny]] = 1
            x, y = nx, ny
        else:
            flag2 = 1
            return

    for b in range(j):
        nx, ny = x + dx[1], y + dy[1]
        if nx >= N or ny < 0:
            flag = 1
            return
        if chk[table[nx][ny]] == 0:
            chk[table[nx][ny]] = 1
            x, y = nx, ny
        else:
            flag = 1
            return

    for c in range(i):
        nx, ny = x + dx[2], y + dy[2]
        if nx < 0 or ny < 0:
            flag2 = 1
            return
        if chk[table[nx][ny]] == 0:
            chk[table[nx][ny]] = 1
            x, y = nx, ny
        else:
            flag2 = 1
            return

    for d in range(j):
        nx, ny = x + dx[3], y + dy[3]
        if nx < 0 or ny >= N:
            flag = 1
            return
        if nx == sx and ny == sy:
            tot = sum(chk)
            if mymax < tot:
                # print(x, y, i, j, chk, tot)
                mymax = tot
            return

        if chk[table[nx][ny]] == 0:
            chk[table[nx][ny]] = 1
            x, y = nx, ny
        else:
            flag = 1
            return

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    mymax = 0

    for x in range(N):
        for y in range(N):
            flag2 = 0
            for i in range(1, N):
                # if flag2: break
                flag = 0
                for j in range(1, N):
                    chk = [0] * 101
                    chk[table[x][y]] = 1

                    Search(x, y, i, j) # 좌표와 모드
                    if flag:
                        break

    if mymax == 0:
        print(f'#{T} {-1}')
    else:
        print(f'#{T} {mymax}')