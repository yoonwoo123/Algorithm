import sys, itertools, copy
sys.stdin = open("벽돌_input.txt")

def Shoot(ball):
    for x in range(H):
        if arr[x][ball] == 0: continue
        if arr[x][ball] == 1:
            arr[x][ball] = 0
            return 0
        else:
            delete.append([x, ball])
            visit[x][ball] = 1 # 방문체크
            find(x, ball)
            return 1
            # 모든 find가 끝나면 Shoot도 끝


def find(x, ball):
    bomb = arr[x][ball] - 1  # 터지는 범위
    # index 오류 방지
    sx = x - bomb
    if sx < 0:
        sx = 0
    ex = x + bomb + 1
    if ex >= H:
        ex = H

    sball = ball - bomb
    if sball < 0:
        sball = 0
    eball = ball + bomb + 1
    if eball >= W:
        eball = W
    # 가로 delete 넣고 세로 delete 넣기
    for j in range(sball, eball):
        if arr[x][j] == 1:
            visit[x][j] = 1
            arr[x][j] = 0
            continue
        if visit[x][j] == 0 and arr[x][j] != 0:
            delete.append([x, j])
            visit[x][j] = 1
            find(x, j)

    for i in range(sx, ex):
        if arr[i][ball] == 1:
            visit[i][ball] = 1
            arr[i][ball] = 0
            continue
        if visit[i][ball] == 0 and arr[i][ball] != 0:
            delete.append([i, ball])
            visit[i][ball] = 1
            find(i, ball)

def down():
    for y in range(W):
        for x in range(H-1, -1, -1):
            if arr[x][y] == 0:
                for k in range(x-1, -1, -1):
                    if arr[k][y] != 0:
                        arr[x][y] = arr[k][y]
                        arr[k][y] = 0
                        break

tc = int(input())
for T in range(1, tc+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(arr)

    visit = [[0 for _ in range(W)] for r in range(H)]
    ori = copy.deepcopy(arr) # 원본 복사해둠
    visitori = copy.deepcopy(visit)

    a = [x for x in range(W)]
    overperm = list(itertools.product(a, repeat=N))
    # print(overperm)
    mymin = 99999
    theend = 0
    for balls in overperm:
        if theend == 1:
            mymin = 0
            break
        for ball in balls:
            delete = [] # 구슬 1개마다 부숴야하는 좌표 리셋
            flag = Shoot(ball)
            # Shoot 함수 끝나면 delete에 있는개수 세고 전부 제거
            if flag: # 첫만난 벽이 1보다 큰수일때만 기능
                for pos in delete:
                    arr[pos[0]][pos[1]] = 0
                tmp = 0
                for x in range(H):
                    for y in range(W):
                        tmp += arr[x][y]
                if tmp == 0:
                    theend = 1
                    break
                # down 함수
                down()
                # visit 초기화해야함
                visit = copy.deepcopy(visitori)
        # 남은 공 개수 세기( 남은공이 가장 적은 경우에 mymin에 넣어줌)
        tot = 0
        for x in range(H):
            for y in range(W):
                if arr[x][y] != 0:
                    tot += 1
        if mymin > tot:
            mymin = tot
        # 중요 ! 그 후 arr 초기화해줘야함 !
        arr = copy.deepcopy(ori)
    print(f'#{T} {mymin}')