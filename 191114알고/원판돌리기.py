import sys, collections
sys.stdin = open("원판돌리기_input.txt")

def ROTATE(x, d, k):
    rcnt = 0
    while True:
        rcnt += 1
        board = (x * rcnt) - 1
        if board <= N-1:
            if d == 0: # 시계
                for _ in range(k):
                    p = table[board].pop()
                    table[board].insert(0, p)
            else:
                for _ in range(k):
                    p = table[board].pop(0)
                    table[board].append(p)
        else:
            break

def BFS(x, y):
    global cnt
    q = collections.deque()
    q.append([x, y])
    v = table[x][y]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N: continue
            if ny < 0:
                ny = M-1
            elif ny >= M:
                ny = 0
            if table[nx][ny] == v:
                table[x][y] = 0
                table[nx][ny] = 0
                q.append([nx, ny])
                cnt += 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

rotates = [list(map(int, input().split())) for i in range(T)]
    # x는 회전하는 원판(행)
    # d = 0 시계방향, d = 1 반시계
    # k 는 회전 횟수

f = 0
for rotate in rotates:
    x, d, k = rotate[0], rotate[1], rotate[2]
    ROTATE(x, d, k)

    # 돌린 후 인접한 것을 찾아서 지워주자 BFS로
    cnt = 0 # 인접한 것을 찾은 횟수 기본값 0
    for x in range(N):
        for y in range(M):
            if table[x][y] > 0:
                BFS(x, y)

    if cnt == 0: # 만약 인접한게 하나도 없었다면
        tot = 0
        tcnt = 0
        for x in range(N):
            for y in range(M):
                if table[x][y] > 0:
                    tot += table[x][y]
                    tcnt += 1
        if tot == 0:
            f = 1
            break
        avg = tot / tcnt
        for x in range(N):
            for y in range(M):
                if table[x][y] > 0:
                    if table[x][y] > avg:
                        table[x][y] -= 1
                    elif table[x][y] < avg:
                        table[x][y] += 1

res = 0
if f:
    print(res)
else:
    for x in range(N):
        for y in range(M):
            res += table[x][y]
    print(res)