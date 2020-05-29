import sys, collections
sys.stdin = open("미네랄_input.txt")
input = sys.stdin.readline

R, C = map(int, input().split())
table = [list(input().strip()) for _ in range(R)]

N = int(input())
cmds = list(map(int, input().split()))

# 짝수는 왼쪽에서 홀수는 오른쪽에서 시작하자.
# 밑에가 비어있어도 옆으로 연결되어있다면 떨어트리면 안된다.
# 즉 형태를 유지한 상태로 떨어트려야한다.
# 미네랄을 부쉈을 때 부순 미네랄과 옆 혹은 위랑 접한 미네랄에
# BFS를 돌려서 바닥과 접하는지 확인후 접하지 않는다면
# 떨어트릴 좌표들을 1칸씩 떨어트리며 땅이나 x를 만날때까지 떨군다.

def BFS(x, y):
    q = collections.deque()
    q.append((x, y))
    visit = [[0 for _ in range(C)] for q in range(R)]
    while q:
        x, y = q.popleft()
        poses.append([x, y])
        visit[x][y] = 1
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C or visit[nx][ny] or table[nx][ny] == '.': continue
            if nx == R-1 and table[nx][ny] == 'x':
                return False # 땅에 붙어 있다.
            visit[nx][ny] = 1
            q.append((nx, ny))
    flag = True
    while flag:
        for i in range(len(poses)):
            px, py = poses[i][0], poses[i][1]
            table[px][py] = '.'
        for i in range(len(poses)):
            px, py = poses[i][0], poses[i][1]
            if (px + 1 >= R or table[px + 1][py] == 'x') and not visit[px+1][py]:
                flag = False
                break
        if flag:
            for i in range(len(poses)):
                poses[i][0] += 1
    for i in range(len(poses)):
        px, py = poses[i][0], poses[i][1]
        table[px][py] = 'x'

cnt = 0
for cmd in cmds:
    cmd -= 1 # idx
    cmd = R - 1 - cmd
    # for g in table:
    #     print(g)
    # print()
    if cnt % 2 == 0:
        for y in range(C):
            if table[cmd][y] == 'x':
                table[cmd][y] = '.'
                poses = []
                if cmd - 1 >= 0 and table[cmd - 1][y] == 'x':
                    BFS(cmd - 1, y)
                poses = []
                if y + 1 < C and table[cmd][y + 1] == 'x':
                    BFS(cmd, y+1)

                break

    else:
        for y in range(C-1, -1, -1):
            if table[cmd][y] == 'x':
                table[cmd][y] = '.'
                poses = []
                if cmd - 1 >= 0 and table[cmd - 1][y] == 'x':
                    BFS(cmd - 1, y)
                poses = []
                if y - 1 >= 0 and table[cmd][y - 1] == 'x':
                    BFS(cmd, y - 1)

                break
    cnt += 1

for g in table:
    print(''.join(g))
print()

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def destroy(i, left):
    i, j = r - i, 0
    if left == 1:
        for k in range(c):
            if a[i][k] == 'x':
                a[i][k] = '.'
                j = k
                break
    else:
        for k in range(c-1, -1, -1):
            if a[i][k] == 'x':
                a[i][k] = '.'
                j = k
                break

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < r and 0 <= nj < c:
            if a[ni][nj] == 'x':
                dq.append([ni, nj])

def bfs(x, y):
    q = deque()
    check = [[0]*c for _ in range(r)]
    fall_list = []
    q.append([x, y])
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == r-1:
            return
        if a[x+1][y] == '.':
            fall_list.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] == 'x' and not check[nx][ny]:
                    check[nx][ny] = 1
                    q.append([nx, ny])

    fall(check, fall_list)

def fall(check, fall_list):
    k, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + k == r-1:
                flag = 1
                break
            if a[i+k+1][j] == 'x' and not check[i+k+1][j]:
                flag = 1
                break
        if flag:
            break
        k += 1

    for i in range(r-2, -1, -1):
        for j in range(c):
            if a[i][j] == 'x' and check[i][j]:
                a[i][j] = '.'
                a[i+k][j] = 'x'

r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
n = int(input())
s = list(map(int, input().split()))
dq = deque()

left = 1
while n:
    index = s.pop(0)
    destroy(index, left)

    while dq:
        x, y = dq.popleft()
        bfs(x, y)

    left *= -1
    n -= 1

for i in range(r):
    for j in range(c):
        print(a[i][j], end='')
    print()