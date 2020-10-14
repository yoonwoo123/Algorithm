import sys, collections
sys.stdin = open("스타트택시_input.txt")

# 택시가 승객과 겹칠 수 있다.
# 택시가 승객을 고르는 우선순위가 올바르게 적용되지 않았을 수 있다.

def searchCustomer(tx, ty, f):
    if table[tx][ty][0] > 1: # 손님이 택시랑 겹침
        customer = table[tx][ty][0]
        table[tx][ty][0] = 0
        return [tx, ty, f, -customer]

    q = collections.deque()
    q.append([tx, ty, f])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[tx][ty] = 1

    while q:
        candidates = []
        if f == 0: return -1
        # print(q)
        for _ in range(len(q)):
            x, y, f = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny][0] == 1 or visited[nx][ny]: continue
                if table[nx][ny][0] == 0: # 빈칸이면
                    q.append([nx, ny, f - 1])
                    visited[nx][ny] = 1

                elif table[nx][ny][0] > 1: # 손님이면
                    customer = table[nx][ny][0]
                    candidates.append([nx, ny, f - 1, -customer])

        if candidates:
            candidates.sort()
            # print(candidates)
            table[candidates[0][0]][candidates[0][1]][0] = 0
            return candidates[0]

    return -1

def goTarget(tx, ty, f, target):
    q = collections.deque()
    q.append([tx, ty, f, 0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[tx][ty] = 1

    while q:
        x, y, f, tot = q.popleft()
        if f == 0: return -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny][0] == 1 or visited[nx][ny]: continue
            if target in table[nx][ny][1]:  # 목적지가 존재한다면
                table[nx][ny][1].pop(table[nx][ny][1].index(target))
                return [nx, ny, (f - 1) + (tot + 1) * 2]

            else:
                q.append([nx, ny, f - 1, tot + 1])
                visited[nx][ny] = 1
    return -1

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)
N, M, Fuel = map(int, input().split())
table = [[[0, []] for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        table[i][j][0] = line[j]

tx, ty = map(int, input().split())
tx -= 1
ty -= 1

# 어떤 손님의 출발지가 다른 손님의 목적지 일 수 있고, 목적지가 겹칠 수 있다.

for i in range(M):
    sx, sy, ex, ey = map(int, input().split())
    table[sx-1][sy-1][0] = i + 2 # 벽이랑 겹치지 않게 손님은 2부터 구분
    table[ex-1][ey-1][1].append(- (i + 2)) # 도착지점은 마이너스 손님번호로

# for g in table:
#     print(g)
# print()

f = Fuel
while True:
    res1 = searchCustomer(tx, ty, f)
    # print('res1', res1)
    if res1 == -1:
        print(-1)
        break
    else:
        res2 = goTarget(res1[0], res1[1], res1[2], res1[3])
        # print('res2', res2)
        if res2 == -1:
            print(-1)
            break

        M -= 1
        if M == 0:
            print(res2[2])
            break

        tx, ty, f = res2