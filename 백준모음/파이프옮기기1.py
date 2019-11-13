import sys, timeit, collections
sys.stdin = open("파이프_input.txt")
start = timeit.default_timer()

# 맵을 탐색하기보단 경우의수를 가져가서 시간단축시키자!

def DFS(x, y, d):
    global tot
    if x == N-1 and y == N-1:
        tot += 1
        return

    if d == 0: # 파이프가 놓여있는 형태 = 가로
        for i in range(2): # 가로, 대각선만
            flag = 1
            if i == 1: # 대각선일 경우는 3군데 체크해줘야한다.
                for j in range(3):
                    nx, ny = x + dx[j], y + dy[j]
                    if nx >= N or ny >= N:
                        flag = 0
                        break
                    if table[nx][ny] == 1:
                        flag = 0
                        break
            if flag == 0: continue

            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N: continue
            if table[nx][ny] == 1: continue
            DFS(nx, ny, i)

    elif d == 2: # 세로
        for i in range(1, 3): # 대각선, 세로만
            flag = 1
            if i == 1:  # 대각선일 경우는 3군데 체크해줘야한다.
                for j in range(3):
                    nx, ny = x + dx[j], y + dy[j]
                    if nx >= N or ny >= N:
                        flag = 0
                        break
                    if table[nx][ny] == 1:
                        flag = 0
                        break
            if flag == 0: continue

            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N: continue
            if table[nx][ny] == 1: continue
            DFS(nx, ny, i)

    else:
        for i in range(3): # 전부
            flag = 1
            if i == 1:  # 대각선일 경우는 3군데 체크해줘야한다.
                for j in range(3):
                    nx, ny = x + dx[j], y + dy[j]
                    if nx >= N or ny >= N:
                        flag = 0
                        break
                    if table[nx][ny] == 1:
                        flag = 0
                        break
            if flag == 0: continue

            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N: continue
            if table[nx][ny] == 1: continue
            DFS(nx, ny, i)

def BFS():
    global tot
    q = collections.deque()
    q.append([sx, sy, d])
    while q:
        x, y, dir = q.popleft()
        if x == N-1 and y == N-1:
            tot += 1
            continue
        for i in range(3):
            if i + dir == 1: continue
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N or table[nx][ny]: continue
            if i == 2 and (table[x + 1][y] or table[x][y + 1]): continue
            q.append([nx, ny, i])

#     0  1  2  가로 세로 대각선
dx = [0, 1, 1]
dy = [1, 0, 1]

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
tot = 0
sx, sy, d = 0, 1, 0 # 파이프 머리부분은 정확히 0,1
# DFS(sx, sy, d)
# if table[N-1][N-1] or (table[N-2][N-1] and table[N-1][N-2] and table[N-2][N-2]):
#     print(0)

# else:
BFS()
print(tot)

# def DFS(x, y, z): # x 좌표 y 좌표 , 파이프의 상태
#     res = 0
#     if x == N-1 and y == N-1:
#         return 1
#     for i in range(3):
#         if i+z == 1: continue # 0(가로) 에서 2(세로)로 못가고 2에서 0으로 못감
#         nx, ny = x + dx[i], y + dy[i]
#         if nx >= N or ny >= N or table[nx][ny]: continue
#         if i == 2 and (table[x][y+1] or table[x+1][y]): continue
#         res += DFS(nx, ny, i)
#     return res
#
# dx = [0, 1, 1]
# dy = [1, 0, 1]
#
# N = int(input())
# table = [list(map(int, list(input().split()))) for _ in range(N)]
#
# print(DFS(0, 1, 0))
stop = timeit.default_timer()
print("time :", stop - start)