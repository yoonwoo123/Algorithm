import sys
sys.stdin = open('input/감시.txt')

def iswall(x, y):
    if x < 0 or x >= N or y < 0 or y >= M: return False
    return True

def fill_cctv(x, y, ct, count):
    for t in ct:
        nx = x + dx[t]
        ny = y + dy[t]
        while iswall(nx, ny) and office[nx][ny] != 6:
            visited[nx][ny] += count
            nx += dx[t]
            ny += dy[t]


def find_cctv(k, n):
    global result
    if k == n:
        cnt = 0
        for x in range(len(office)):
            for y in range(len(office[x])):
                if not office[x][y] and not visited[x][y]:
                    cnt += 1
        result = min(result, cnt)

    else:
        x, y, cctv_type = cctv[k]
        for ct in dir[cctv_type]:
            fill_cctv(x, y, ct, 1)
            find_cctv(k+1, n)
            fill_cctv(x, y, ct, -1)


N, M = map(int, input().split())
office = [list(map(int, input().split()))for _ in range(N)]
cctv = []
result = [[-1]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = [ [[0]],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]
for x in range(len(office)):
    for y in range(len(office[x])):
        if office[x][y] and office[x][y] != 6:
            cctv.append([x, y, office[x][y]])
result = 64
find_cctv(0, len(cctv))
