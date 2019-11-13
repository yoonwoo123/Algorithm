import sys, itertools, collections, copy
sys.stdin = open("캐슬디펜스_input.txt")

def BFS(sniper):
    q = collections.deque([])
    # for s in snipers:
    q.append([N, sniper, 0])
    while q:
        x, y, cnt = q.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if cnt >= D: break # 사거리제한
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if table[nx][ny] == 1: # 죽일병사위치체크
                chk.append([nx, ny])
                return
            else:
                q.append([nx, ny, cnt + 1])
N, M, D = map(int, sys.stdin.readline().split())

dx = [0, -1, 0]
dy = [-1, 0, 1]

table = collections.deque([])

for _ in range(N):
    table.append(list(map(int, list(sys.stdin.readline().split()))))
table.extend([[2]*M]) # 성벽 추가

origin = copy.deepcopy(table)
# print(origin)
# print(table)
a = [x for x in range(M)]
comb = list(itertools.combinations(a, 3))
# print(comb)
mymax = -1
# my = []
for snipers in comb:
    kill = 0
    while True:
        chk = [] # 체크박스초기화
        for sniper in snipers:
            BFS(sniper)
        # 체크박스에 있는 병사를 죽이고 개수를 셈
        for c in chk:
            if table[c[0]][c[1]] != 0:
                table[c[0]][c[1]] = 0
                kill += 1

        # 조합중 1분대 공격이 끝났으므로 맵을 1칸씩 내림.
        table.pop()
        table.appendleft([0] * 5)
        for i in range(M):
            table[N][i] = 2
        # 적이모두죽었나 확인
        tot = 0
        for x in range(N):
            for y in range(M):
                tot += table[x][y]
        if tot == 0: # 모두 죽으면 while 빠짐
            break
    # 모두죽인 테이블인 맵을 원래대로 초기화
    table = copy.deepcopy(origin)
    # print(table)
    # my.append(kill)
    if mymax < kill:
        mymax = kill
# print(my)
print(mymax)