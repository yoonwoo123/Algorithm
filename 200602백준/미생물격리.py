import sys, collections
sys.stdin = open("미생물격리_input.txt")

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
mir = [0, 2, 1, 4, 3]
tc = int(input())
for T in range(1, tc+1):
    N, M, K = map(int, input().split())
    table = [[[0, 0] for _ in range(N)] for q in range(N)]
    cells = []
    for _ in range(K):
        posx, posy, nums, dir = map(int, input().split())
        table[posx][posy][0] = nums
        table[posx][posy][1] = dir
        cells.append([posx, posy])

    for g in table:
        print(g)
    print()
    for _ in range(M):
        tmp = []
        for i in range(K):
            x = cells[i][0]
            y = cells[i][1]
            nums = table[x][y][0]
            dir = table[x][y][1]

            nx, ny = x + dx[dir], y + dy[dir]
            tmp.append([nx, ny, nums, dir]) # 옮길곳의 좌표값과 미생물수, 방향 저장
            table[x][y][0], table[x][y][1] = 0, 0
            cells[i][0] = nx
            cells[i][1] = ny

        duple = []
        tot = []
        for i in range(K):
            nx = tmp[i][0]
            ny = tmp[i][1]
            nums = tmp[i][2]
            dir = tmp[i][3]

            ## 미생물 이동 ##
            if table[nx][ny][0] > 0: # 미생물이 겹친 경우
                flag = 1
                for t in tot: # tot을 미생물의 총합으로 만드는 과정
                    if nx == t[0] and ny == t[1]:
                        t[2] += nums
                        flag = 0
                        break
                if flag:
                    tot.append([nx, ny, table[nx][ny][0] + nums])

                if table[nx][ny][0] < nums:
                    table[nx][ny][0] = nums # 나중에 총합으로 업뎃해야함
                    table[nx][ny][1] = dir
                duple.append(i) # 겹친 미생물 좌표의 인덱스저장
            else:
                table[nx][ny][1] = dir
                table[nx][ny][0] += nums
            #########

            if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                dir = mir[dir]
                table[nx][ny][0] //= 2 # 절반이 죽음
                table[nx][ny][1] = dir
                if table[nx][ny][0] == 0: # 전부 죽으면
                    duple.append(i)
                    table[nx][ny][1] = 0

        for t in tot: # 미생물 합쳐진 총합으로 업데이트
            table[t[0]][t[1]][0] = t[2]

        for i in range(len(duple)): # 겹친 미생물 안쓰이는것들 pop
            cells.pop(duple[i] - i)
            K -= 1

    res = 0
    for x in range(N):
        for y in range(N):
            res += table[x][y][0]
    print(f'#{T} {res}')