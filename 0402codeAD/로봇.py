import sys, collections, itertools
sys.stdin = open("로봇_input.txt")

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[[0]*4 for _ in range(m)] for _ in range(n)] # 2차원이 4개 쌓여있는 직육면체
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0) # 동 서 남 북
# for x in range(n):
#     for y in dist[x]:
#         print(y)

def bfs():
    q = collections.deque()
    q.append((sx-1, sy-1, sd-1))
    while q:
        x, y, d = q.popleft()
        if x == ex-1 and y == ey-1 and d == ed-1:
            print(dist[x][y][d])
            return
        for i in range(1, 4): # go1, go2, go3
            nx, ny = x+dx[d]*i, y+dy[d]*i
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if a[nx][ny]: # a[nx][ny] == 0 이면 통과
                break       #아니면 break
            if not dist[nx][ny][d]: # 방문하지 않았다면
                q.append((nx, ny, d))
                dist[nx][ny][d] = dist[x][y][d]+1 # 카운트를 1개 증가 도착지점 카운트가 최소로뽑힐수밖에 없다.

        for i in range(4): # 방향을 바꿔주는 명령
            if i == d: # 현재 방향 외의 3방향을 해줘야하므로 continue
                continue
            if (i+d)%4 == 1: # i+d의 나머지가 1이면 동 > 서 , 남 > 북 이런 식이므로 명령 2번
                k = 2
            else:
                k = 1

            if not dist[x][y][i]: # 방문하지 않았다면
                q.append((x, y, i))
                dist[x][y][i] = dist[x][y][d]+k

bfs()

# def BFS():
#     que = []
#     que.append([sx, sy, sd])
#     while que:
#         x, y, d = que.pop(0)
#         if dx[dir]
#         for i in range(1, 5):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= X or ny >= Y: continue


#        1  2  3   4
# dx = [0, 0, 0, 1, -1] # 우 좌 하 상
# dy = [0, 1, -1, 0, 0]
# direction = [1, 2, 3, 4] # 동 서 남 북
# turn = [0 for _ in range(5)]
#
# turn[1] = [4, 3]
# turn[2] = [3, 4]
# turn[3] = [1, 2]
# turn[4] = [2, 1]
#
# for g in turn:
#     print(g)
# print()
#
# X, Y = map(int, input().split())
# arr = []
# for i in range(X):
#     arr.append(list(map(int, input().split())))
# # 1은 벽 0만 다닐수 있다.
# sx, sy, sd = map(int, input().split())
# ex, ey, ed = map(int, input().split())

