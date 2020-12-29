import sys, collections, copy
sys.stdin = open("아맞다우산_input.txt")
input = sys.stdin.readline

def BFS(visited):
    q = collections.deque()
    visited[sx][sy][0] = 1
    q.append((sx, sy, 0, visited))

    while q:
        for _ in range(len(q)):
            x, y, time, visited = q.popleft()
            if x == ex and y == ey and sum(visited[x][y][1:]) == len(items):
                # print('!', findNum, items)
                return time
            # print(x, y, time)
            # for g in visited:
            #     print(g)
            # print()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= M or ny >= N or table[nx][ny] == '#': continue

                arr = check(visited[nx][ny], visited[x][y])
                if arr:
                    copyVisit = copy.deepcopy(visited)
                    copyVisit[nx][ny] = arr
                    q.append((nx, ny, time + 1, copyVisit))

def check(next, curr):
    flag = False

    for i in range(len(items) + 1):
        if next[i] == 0 and curr[i] == 1:
            next[i] = 1
            flag = True

    if flag:
        return next

    return False

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
N, M = map(int, input().split())
table = []
items = {}

cnt = 1
for i in range(M):
    line = list(input().strip())
    table.append(line)
    for j in range(N):
        if line[j] == 'S':
            sx, sy = i, j

        elif line[j] == 'E':
            ex, ey = i, j

        elif line[j] == 'X':
            items[(i, j)] = cnt
            cnt += 1

visited = [[[0 for _ in range(len(items) + 1)] for _ in range(N)] for _ in range(M)]

for (x, y), v in items.items():
    visited[x][y][v] = 1

print(BFS(visited))