import sys, collections
sys.stdin = open("연구소_input.txt")

def BFS():
    global zcnt, mymax
    q = collections.deque()
    for i in range(len(vpos)):
        q.append([vpos[i][0], vpos[i][1]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if table[nx][ny]: continue
            else:
                table[nx][ny] = 2
                q.append([nx, ny])
                visit.append([nx, ny])
                zcnt -= 1
                if mymax >= zcnt: return

def DFS(dep):
    global zcnt, mymax, visit

    if dep == 3:
        BFS()
        if mymax < zcnt:
            mymax = zcnt

        for v in visit:
            table[v[0]][v[1]] = 0
        zcnt = oz
        visit = []
        return

    for x in range(N):
        for y in range(M):
            if table[x][y] == 0:
                table[x][y] = 1
                DFS(dep + 1)
                table[x][y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
table = []
vpos = []
zcnt = 0
mymax = -1
visit = []

for x in range(N):
    table.append(list(map(int, input().split())))
    for y in range(M):
        if table[x][y] == 2:
            vpos.append([x, y])
        elif table[x][y] == 0:
            zcnt += 1
zcnt -= 3 # 벽을 세울것이기 때문에 미리 3뺌
oz = zcnt
DFS(0)
print(mymax)