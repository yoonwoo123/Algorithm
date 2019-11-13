import sys, copy, time, collections
sys.stdin = open("줄기세포_input.txt")
# 2 - 비활성, 1 - 활성, 0 - 죽음

def BFS():
    global res
    q = collections.deque()
    for w in range(len(cells)): # x, y, value, condition, cnt, time
        q.append([cells[w][0], cells[w][1], cells[w][2], cells[w][3], 0, 0])
    while q:
        x, y, v, c, cnt, time = q.popleft()
        # print(time)

        if time == K + 1:
            res = len(q) + 1
            return

        if c == 1: # 활성화상태면
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if table[nx][ny][0] == 0:
                    table[nx][ny][0] = v
                    table[nx][ny][1] = 2
                    q.append([nx, ny, v, 2, 0, time + 1])
                elif table[nx][ny][1] == 2 and table[nx][ny][0] < v:
                    table[nx][ny][0] = v
                    table[nx][ny][1] = 2
                    q.append([nx, ny, v, 2, 0, time + 1])

        cnt += 1

        if cnt == v:
            c -= 1
            if c == 0: continue # 죽음
            cnt = 0

        if c == 2:
            q.append([x, y, v, c, cnt, time + 1])


        elif c == 1:
            q.append([x, y, v, c, cnt, time + 1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())
for T in range(1, tc+1):
    X, Y, K = map(int, input().split())
    table = [[[0] * 2 for _ in range(Y+K+20)] for q in range(X+K+20)]
    cells = []
    res = 0

    for x in range((X+K+20)//2-1, (X+K+20)//2 + X-1):
        tmp = list(map(int, input().split()))
        for y in range((Y+K+20)//2-1, (Y+K+20)//2 + Y-1):
            table[x][y][0] = tmp[y-(Y+K+20)//2-1] # value
            table[x][y][1] = 2 # condition 비활성
            if table[x][y][0]:
                cells.append([x, y, table[x][y][0], 2])
    BFS()
    print('res:', res)
    tot = 0
    for x in range((X + K + 20) // 2 - 1, (X + K + 20) // 2 + X - 1):
        for y in range((Y + K + 20) // 2 - 1, (Y + K + 20) // 2 + Y - 1):
            if table[x][y][1] > 0 and table[x][y][0] > 0:
                tot += 1
    print('tot:', tot)
    for g in table:
        print(g)
    print()