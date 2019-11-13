import sys
sys.stdin = open("핀볼_input.txt")

def DFS(x, y, dir, cnt):
    # print('시작')
    # print([x, y])
    global mymax, s, e
    # if visit[x][y][0] == dir and visit[x][y][1] <= cnt:
    #     return
    # if visit[x][y] != [-1, -1]: # 방문을 안했을때만 방문체크
    #     visit[x][y] = [dir, cnt]
    while True:
        nx, ny = x + dx[dir], y + dy[dir]

        if table[nx][ny] == 11:
            # print([s, e, cnt])
            if mymax < cnt:
                mymax = cnt
            return

        if table[nx][ny] == -1:
            # print([s, e, cnt])
            if mymax < cnt:
                mymax = cnt
            return

        if table[nx][ny] == 0:
            # print('0 만나 진행')
            x, y = nx, ny
            # if visit[x][y][0] == dir and visit[x][y][1] <= cnt:
            #     return
            # if visit[x][y] != [-1, -1]:
            #     visit[nx][ny] = [dir, cnt]
            continue

        if table[nx][ny] == 1:
            if dir == 1:
                dir = 3
                x, y = nx, ny
            elif dir == 2:
                dir = 0
                x, y = nx, ny
            elif dir == 0:
                dir = 1
                x, y = nx, ny
            elif dir == 3:
                dir = 2
                x, y = nx, ny

            cnt += 1
            continue

        elif table[nx][ny] == 2:
            if dir == 0:
                dir = 3
                x, y = nx, ny
            elif dir == 1:
                dir = 0
                x, y = nx, ny
            elif dir == 2:
                dir = 1
                x, y = nx, ny
            elif dir == 3:
                dir = 2
                x, y = nx, ny
            cnt += 1
            continue

        elif table[nx][ny] == 3:
            if dir == 0:
                dir = 2
                x, y = nx, ny
            elif dir == 1:
                dir = 0
                x, y = nx, ny
            elif dir == 2:
                dir = 3
                x, y = nx, ny
            elif dir == 3:
                dir = 1
                x, y = nx, ny
            cnt += 1
            continue

        elif table[nx][ny] == 4:
            if dir == 0:
                dir = 1
                x, y = nx, ny
            elif dir == 1:
                dir = 2
                x, y = nx, ny
            elif dir == 2:
                dir = 3
                x, y = nx, ny
            elif dir == 3:
                dir = 0
                x, y = nx, ny
            cnt += 1
            continue

        elif table[nx][ny] == 5:
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 2
            cnt += 1
            x, y = nx, ny
            continue

        elif table[nx][ny] == 6:
            for i in range(2):
                if six[i][0] == nx and six[i][1] == ny:
                    nx, ny = six[(i + 1) % 2]
                    break
            x, y = nx, ny
            continue

        elif table[nx][ny] == 7:
            for i in range(2):
                if sev[i][0] == nx and sev[i][1] == ny:
                    nx, ny = sev[(i + 1) % 2]
                    break
            x, y = nx, ny
            continue

        elif table[nx][ny] == 8:
            for i in range(2):
                if eig[i][0] == nx and eig[i][1] == ny:
                    nx, ny = eig[(i + 1) % 2]
                    break
            x, y = nx, ny
            continue

        elif table[nx][ny] == 9:
            for i in range(2):
                if nin[i][0] == nx and nin[i][1] == ny:
                    nx, ny = nin[(i + 1) % 2]
                    break
            x, y = nx, ny
            continue

        elif table[nx][ny] == 10:
            for i in range(2):
                if ten[i][0] == nx and ten[i][1] == ny:
                    nx, ny = ten[(i + 1) % 2]
                    break
            x, y = nx, ny
            continue

tc = int(input())
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

for T in range(1, tc+1):
    N = int(input())
    # table = []
    mymax = -1
    # blackhole = []
    six = []
    sev = []
    eig = []
    nin = []
    ten = []

    table = [[5 for _ in range(N+2)] for q in range(N+2)]
    # print(table)
    visit = [[[-1]*2 for _ in range(N)] for q in range(N)]
    # print(visit)
    # 웜홀의 좌표는 테이블 만들 때 미리 찾아두자
    for x in range(N):
        tmp = list(map(int, input().split()))
        for y in range(N):
            table[x+1][y+1] = tmp[y]
            # if table[x][y] == -1:
            #     blackhole.append([x, y])
            if tmp[y] == 6:
                six.append([x+1, y+1])
            elif tmp[y] == 7:
                sev.append([x+1, y+1])
            elif tmp[y] == 8:
                eig.append([x+1, y+1])
            elif tmp[y] == 9:
                nin.append([x+1, y+1])
            elif tmp[y] == 10:
                ten.append([x+1, y+1])
    # print(sev)
    # for g in table:
    #     print(g)
    # print()
    for x in range(1, N+1):
        for y in range(1, N+1):
            if table[x][y] == 0:
                s, e = x, y
                table[s][e] = 11
                for d in range(4):
                    DFS(x, y, d, 0)
                    # print('방향하나끝')
                # print([s, e, mymax])
                table[s][e] = 0
    print(f'#{T} {mymax}')