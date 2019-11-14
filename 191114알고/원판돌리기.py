import sys, collections
sys.stdin = open("원판돌리기_input.txt")

def ROTATE(x, d, k):
    cnt = 0
    while True:
        cnt += 1
        board = (x * cnt) - 1
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
            if nx < 0 or nx >= N : continue
            if ny == -1:
                ny = M-1
            elif ny == M:
                ny = 0
            if table[nx][ny] == v:
                table[x][y] = 0
                table[nx][ny] = 0
                q.append([nx, ny])
                cnt += 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M, T = map(int, input().split())
table = []

for i in range(N):
    table.append(list(map(int, input().split())))

rotates = []
for i in range(T):
    x, d, k = map(int, input().split())
    rotates.append([x, d, k])
    # x는 회전하는 원판(행)
    # d = 0 시계방향, d = 1 반시계
    # k 는 회전 횟수

# 여기서 중요한 것은 인접하다고 바로 삭제하는것이 아닌
# 삭제하기전에 인접한것을 전부 찾아놓고 한번에삭제하자.

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
                if table[x][y]:
                    tot += table[x][y]
                    tcnt += 1
        avg = tot / tcnt
        for x in range(N):
            for y in range(M):
                if table[x][y] > 0:
                    if table[x][y] > avg:
                        table[x][y] -= 1
                    elif table[x][y] < avg:
                        table[x][y] += 1

res = 0
for x in range(N):
    for y in range(M):
        res += table[x][y]

print(res)