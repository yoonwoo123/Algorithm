import sys, collections
sys.stdin = open("토마토2_input.txt")

def BFS():
    global my_min
    que = collections.deque([])
    for i in range(int(len(tmt)//3)):
        que.append([tmt[3*i], tmt[3*i+1], tmt[3*i+2], 0])
    while que:
        x, y, z, time = que.popleft()
        # print(time)
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if nx < 0 or nx >= X or ny < 0 or ny >= Y or nz < 0 or nz >= H:
                continue
            if arr[nz][nx][ny] == -1:
                continue

            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = time+1
                que.append([nx, ny, nz, time + 1])
                # continue

            # elif arr[nx][ny] >= time+1:
            #     arr[nx][ny] = time+1 # 방문체크를 1이 아닌 걸리는 시간으로 함
            #     que.append([nx, ny, time + 1])
    if my_min > time:
        my_min = time
    # sum(days) == 0 이면 0 출력

def tmtchk():
    global flag
    for z in range(H):
        for x in range(X):
            for y in range(Y):
                if arr[z][x][y] == 0:
                    flag = -1
                    return

dx = [-1, 1, 0, 0, 0, 0] # 가로
dy = [0, 0, -1, 1, 0, 0] # 세로
dz = [0, 0, 0, 0, -1, 1] # 높이

Y, X, H = map(int, input().split())
arr = []
my_min = 999999999999
for h in range(H):
    tmp = []
    for i in range(X):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)
# 1 익음 0 익지않음 -1 없음
# 익은토마토 1이 바이러스처럼 출발지점
# 익은토마토는 상자에 여러개 있을 수있다.
# 익은토마토가 모든 안익은 0을 1로 만들때 걸리는 최소시간 = max(days)
# 먼저 익은토마토만 있는경우는 0을 출력하자. -> BFS돌려서 flag ==0일떄
# 다 못 익는 경우는 BFS돌리고 난후 0이 남았나 확인후 남았으면 -1 출력
# print(arr)

tmt = []
for z in range(H):
    for x in range(X):
        for y in range(Y):
            if arr[z][x][y] == 1:
                tmt.append(x)
                tmt.append(y)
                tmt.append(z)
# print(tmt)
# for i in range(len(tmt)//2):
#     BFS(tmt[i*2], tmt[i*2 + 1])
BFS()
# print(tmt)
# print(days)
flag = 0
tmtchk()
if flag == -1:
    print(-1)
else:
    print(my_min)