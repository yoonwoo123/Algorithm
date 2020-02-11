import sys, collections
sys.stdin = open("말이되고픈원숭이_input.txt")
input = sys.stdin.readline

def BFS():
    q.append((0, 0, 0)) # x, y, 점프한 횟수
    while q:
        x, y, k = q.popleft()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= H or ny >= W or dist[nx][ny][k] or table[nx][ny]: continue
            if nx == H-1 and ny == W-1:
                print(dist[x][y][k])
                return
            dist[nx][ny][k] = dist[x][y][k] + 1
            q.append((nx, ny, k))

        if k == K: continue
        for dx, dy in ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= H or ny >= W or dist[nx][ny][k+1] or table[nx][ny]: continue
            if nx == H - 1 and ny == W - 1:
                print(dist[x][y][k])
                return
            dist[nx][ny][k+1] = dist[x][y][k] + 1
            q.append((nx, ny, k+1))
    print(-1)

K = int(input())
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]
dist = [[[0 for z in range(K+1)] for y in range(W)] for x in range(H)]
dist[0][0][0] = 1
q = collections.deque()
BFS()