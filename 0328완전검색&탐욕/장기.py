import sys, collections
sys.stdin = open("장기_input.txt")
# BFS

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(x, y, cnt):
    global res
    que = []
    que.append([x, y, 1])
    arr[x][y] = 1 # 방문 표시
    while que:
        x, y, cnt = que.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if arr[nx][ny] == 1: continue
            if arr[nx][ny] == 2:
                res = cnt
                return
            que.append([nx, ny, cnt+1])
            arr[nx][ny] = 1
# def DFS(x, y, cnt):
#     global res
#     if res <= cnt:
#         return
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
#         if arr[nx][ny] == 1: continue
#         if arr[nx][ny] == 2:
#             if res > cnt:
#                 res = cnt
#             return
#         arr[nx][ny] = 1
#         DFS(nx, ny, cnt+1)

N, M = map(int, input().split())
HX, HY, X, Y = map(int, input().split())
HX -= 1
HY -= 1
X -= 1
Y -= 1
arr = [[0 for _ in range(M)] for _ in range(N)]
arr[HX][HY] = 1 # 말
arr[X][Y] = 2 # 졸병
res = 0

if HX == X and HY == Y:
    print(0)
else:
    BFS(HX, HY, 1)
    for g in arr:
        print(g)
    print()
    print(res)