import sys, collections
sys.stdin = open("구슬_input.txt")

# . 이동가능지역 , # 벽 , H 목표구멍
# 실패가 될수밖에없으면 -1 출력

def BFS():
    global rx, ry, bx, by, solx, soly, sol
    que = collections.deque([])
    que.append([rx, ry, bx, by, 0])
    while que:
        rx, ry, bx, by, time = que.popleft()

        for i in range(4):

            # if time >= 10:
            #     return -1

            chk = [0, 0] # r, b
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]
            # if arr[nrx][nry] == '#':
            #     chk[0] = 1
            # if arr[nbx][nby] == '#':
            #     chk[1] = 1
            # if chk[0] == 1 and chk[1] ==1: continue
            if nbx == nrx and nby == nry: continue
            if arr[nbx][nby] == 'H': continue
            if arr[nrx][nry] == '#' and arr[nbx][nby] == '#': continue
            if arr[nrx][nry] == '.' and arr[nbx][nby] == '.':
                arr[rx][ry] = '.'
                arr[bx][by] = '.' # 움직이면 원래있었던 자리 .으로
                que.append([nrx, nry, nbx, nby, time + 1])
                if memo[nrx][nry] > memo[rx][ry] + 1:
                    memo[nrx][nry] = memo[rx][ry] + 1
            elif arr[nrx][nry] == '.' and arr[nbx][nby] == '#':
                arr[rx][ry] = '.'
                que.append([nrx, nry, bx, by, time + 1])
                if memo[nrx][nry] > memo[rx][ry] + 1:
                    memo[nrx][nry] = memo[rx][ry] + 1
            elif arr[nrx][nry] == '#' and arr[nbx][nby] == '.':
                arr[bx][by] = '.'
                que.append([rx, ry, nbx, nby, time + 1])
                if memo[nrx][nry] > memo[rx][ry] + 1:
                    memo[nrx][nry] = memo[rx][ry] + 1
            elif arr[nrx][nry] == 'H':
                solx = rx
                soly = ry
                sol = time + 1
                return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())
for T in range(1, tc+1):
    X, Y = map(int, input().split())
    memo = [[99 for _ in range(Y)] for _ in range(X)]
    arr = []
    for i in range(X):
        arr.append(list(input()))
    f = 0
    for x in range(X):
        if f == 3: break
        for y in range(Y):
            if f == 3: break
            if arr[x][y] == 'R':
                rx, ry = x, y
                f += 1
            elif arr[x][y] == 'B':
                bx, by = x, y
                f += 1
            elif arr[x][y] == 'H':
                ex, ey = x, y
                f += 1

    memo[rx][ry] = 0
    solx = 0
    soly = 0
    sol = 0
    BFS()
    if sol > 10:
        print(memo[solx][soly] + 1)
    else:
        print(sol)

    # for g in memo:
    #     print(g)
    # print()
    # print(arr)
