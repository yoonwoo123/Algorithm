import sys
sys.stdin = open("새로운게임2_input.txt")

# 빨강(1)이면 pop() 한 순서대로 append
# 흰색(0)이면 pop() 하고 insert(0, p) 로 넣어야함

def MOVE(i, x, y, d):
    global res
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] == 2:
        # 원래 가고자 하는 방향의 반대로 nx, ny를 구하고 그 nx, ny가
            # if 범위를 또 벗어나거나 또 파랑색이면 말의 방향만 갱신
            # else nx, ny, d 의 값을 horese 에 갱신
        d = mir[d]
        hposes[i][2] = d  # 방향 갱신
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] == 2:
            return
        elif table[nx][ny] == 0: # 흰색
            L = len(htable[nx][ny]) # 이미 말이 있을 경우 생각
            while True:
                p = htable[x][y].pop()
                htable[nx][ny].insert(L, p)
                hposes[p][0], hposes[p][1] = nx, ny
                if len(htable[nx][ny]) >= 4:
                    res = 0
                    return
                if p == i: return
        else: # 빨강
            while True:
                p = htable[x][y].pop()
                htable[nx][ny].append(p)
                hposes[p][0], hposes[p][1] = nx, ny
                if len(htable[nx][ny]) >= 4:
                    res = 0
                    return
                if p == i: return

    elif table[nx][ny] == 0: # 흰색
        L = len(htable[nx][ny])  # 이미 말이 있을 경우 생각
        while True:
            p = htable[x][y].pop()
            htable[nx][ny].insert(L, p)
            hposes[p][0], hposes[p][1] = nx, ny
            if len(htable[nx][ny]) >= 4:
                res = 0
                return
            if p == i: return

    else:  # 빨강
        while True:
            p = htable[x][y].pop()
            htable[nx][ny].append(p)
            hposes[p][0], hposes[p][1] = nx, ny
            if len(htable[nx][ny]) >= 4:
                res = 0
                return
            if p == i: return

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

mir = [1, 0, 3, 2]

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
# 0은 흰색, 1은 빨강, 2나 범위밖은 파랑

hposes = []
htable = [[[] for _ in range(N)] for q in range(N)] # 말의 위치 표시 맵 3차원으로 쌓일수있게

for i in range(K):
    x, y, d = map(int, input().split())
    hposes.append([x-1, y-1, d-1])
    htable[x-1][y-1].append(i)

t = 1
res = -1 # 답
while t < 1001:
    for i in range(K): # i 는 말의 번호 0, 1, 2 ...
        x, y, d = hposes[i][0], hposes[i][1], hposes[i][2]
        MOVE(i, x, y, d)
        if res != -1:
            res = t
            break
    if res != -1:
        break
    t += 1
print(res)