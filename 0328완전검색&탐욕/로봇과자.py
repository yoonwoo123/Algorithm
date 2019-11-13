import sys
sys.stdin = open("로봇과자_input.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def perm(n, r): # n= 3, r = 0 # n은 구하고자하는 수 , r = 0 부터 올라감
    global final, result

    if r == N-1:
        if final <= result:
            return
        result = 0
        for i in range(N):
            BFS(rpos[i][0], rpos[i][1], spos[i][0], spos[i][1], 1)
            result += res
        if final > result:
            final = result

        # total.append(result)
        # print(final)
        # print(spos)
    else:
        for i in range(r, n): # 0,1,2
            spos[i], spos[r] = spos[r], spos[i]
            perm(n , r + 1)
            spos[i], spos[r] = spos[r], spos[i]



def BFS(x, y, ex, ey, cnt): # cnt = 1로시작
    global res
    que = []
    que.append([x, y, cnt])
    while que:
        x, y, cnt = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 100 or ny < 0 or ny >= 100: continue
            # if arr[nx][ny] == 1: continue

            if nx == ex and ny == ey:
                res = cnt
                return
            arr[nx][ny] = 1 # 방문체크
            que.append([nx, ny, cnt+1])


tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    snacks = list(map(int, input().split()))
    robots = list(map(int, input().split()))
    spos = []
    rpos = []
    all = []
    final = 99999999999
    res = 0
    #  과자 = 2, 로봇 = 1
    for i in range(N):
        x = snacks[i*2]
        y = snacks[i*2 +1]
        arr[x][y] = 2
        spos.append([x, y])

    for i in range(N):
        x = robots[i*2]
        y = robots[i*2 +1]
        arr[x][y] = 1
        rpos.append([x, y])
    # print(rpos)
    # print(spos)


    total = []
    result = 0
    # 로봇이 다른스낵으로 가는 경우까지 전부 생각

    # for i in range(N):
    #     BFS(rpos[i][0], rpos[i][1], spos[i][0], spos[i][1], 1)
    #     result += res
    # total.append(result)
    # print(total)
    perm(N, 0)
    print(final)

