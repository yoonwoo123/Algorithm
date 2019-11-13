import sys, collections, copy, itertools
sys.stdin = open("다리만들기2_input.txt")

def BFS(x, y, lcnt): # 섬의 개수와 좌표 찾아주기
    q = collections.deque()
    q.append([x, y])
    table[x][y] = 0
    lands[lcnt].append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if table[nx][ny]:
                lands[lcnt].append([nx, ny]) # 3차원 배열로 섬의 좌표 저장
                table[nx][ny] = 0
                q.append([nx, ny])

def Search(x, y, num): # 섬과 섬 사이의 최소길이 다리 길이 구하자.
    sx, sy = x, y
    for i in range(4):
        x, y = sx, sy
        while True:
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: break
            if table[nx][ny] == num: break # 자기섬과같다면
            if table[nx][ny] == 0: # 바다라면
                x, y = nx, ny
                continue

            if table[nx][ny]:
                landnum = table[nx][ny] # 찾은섬 번호
                dist = abs(nx - sx) + abs(ny - sy) - 1 # 연결하는다리길이
                if dist < 2: break # 2보다 작은건 기록할필요없다.
                if graph[num][landnum] == 0:
                    graph[num][landnum] = dist
                    graph[landnum][num] = dist
                    sums[num] = 1
                    sums[landnum] = 1
                elif graph[num][landnum] > dist: # 이러면 최소값유지
                    graph[num][landnum] = dist
                    graph[landnum][num] = dist # 쌍방향으로 표시
                    sums[num] = 1
                    sums[landnum] = 1
                break

def DFS(x): # 모든 섬이 인접해 있는지 체크
    global flag, chk, tot
    cb = 0
    for i in range(1, lcnt + 1):
        if chk[i] == 0:
            cb = 1
            break
    if cb == 0:
        flag = 1
        return flag

    for y in range(1, lcnt + 1):
        if graph[x][y] > 1:
            chk[y] = 1  # 체크 횟수
            tot += graph[x][y]
            graph[x][y], graph[y][x] = 0, 0  # 방문체크로 지워줌
            DFS(y)

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1, 1]
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
lands = [[], [], [], [], [], [], []] # 0 ~ 6 빈배열 7개
# 섬의 개수는 2<= 섬 <= 6
lcnt = 0 # 섬의 개수

for x in range(N):
    for y in range(M):
        if table[x][y]:
            lcnt += 1
            BFS(x, y, lcnt)

for i in range(1, lcnt+1):
    for pos in lands[i]:
        table[pos[0]][pos[1]] = i # 몇번째섬인지 지도에 1,2,3,4 로 표시

graph = [[0 for _ in range(lcnt+1)] for q in range(lcnt+1)]

sums = [0] * (lcnt + 1)
for i in range(1, lcnt): # 섬이 4개면 섬3개만 돌려보면된다.
    for pos in lands[i]: # 최소길이의 다리를 잇는법을 찾자
        Search(pos[0], pos[1], i) # x, y, 돌리는 섬번호
ori = copy.deepcopy(graph)
lon = 0
for i in range(1, lcnt+1):
    if sums[i] == 0:
        lon = 1 # 다리가 하나도 이어지지 못한 외딴 섬이 있다면 바로 -1 출력

gpos = []
for x in range(1, lcnt+1):
    for y in range(1, x+1):
        if graph[x][y]:
            gpos.append([x, y]) # 그래프에서 노드의 좌표값을 구함

bcnt = len(gpos)# 만들 수 있는 모든 다리의 개수
mymin = 999999
if lon or bcnt < lcnt - 1:
    print(-1)
elif bcnt == lcnt - 1:
    flag = 0
    chk = [0] * 7 # 섬이 최대 6개이므로
    tot = 0
    chk[gpos[0][0]] = 1
    DFS(gpos[0][0])

    if flag:
        if mymin > tot:
            mymin = tot
        print(mymin)
    else:
        print(-1)
else:
    # 다리가 N-1보다 넘치는 만큼 조합으로 뽑아서 0으로 만듬
    a = [x for x in range(bcnt)]
    comb = list(itertools.combinations(a, (bcnt - lcnt + 1)))
    for bridges in comb:
        flag = 0
        chk = [0] * 7
        for b in bridges:
            graph[ gpos[b][0] ][ gpos[b][1] ] = 0
            graph[ gpos[b][1] ][ gpos[b][0] ] = 0
        tot = 0 # 다리 길이
        chk[gpos[bridges[0]-1][0]] = 1
        DFS(gpos[bridges[0]-1][0])
        if flag:
            if mymin > tot:
                mymin = tot
        graph = copy.deepcopy(ori) # 그래프 초기화
    if mymin == 999999:
        print(-1)
    else:
        print(mymin)
