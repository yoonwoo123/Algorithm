import copy

def DFS(x, team):
    global flag, chk
    n = len(team)
    if sum(chk) == n:
        flag = 1
        return flag

    for y in range(1, N+1):
        if table[x][y] == 1 and y in team:
            chk[y] = 1 # 체크 횟수
            table[x][y], table[y][x] = 0, 0 # 방문체크로 지워줌
            # print(team)
            # for g in table:
            #     print(g)
            # print()
            DFS(y, team)
            # table[x][y], table[y][x] = 1, 1 # 지운거 살려줌
            # chk[x] = 0


def split(dep):
    global mymin, table, flag, chk
    if dep == N:
        teamA = []
        teamB = []
        for i in range(1, N+1):
            if A[i] == 0:
                teamA.append(i)
            else:
                teamB.append(i)
        alen = len(teamA)
        blen = len(teamB)
        if alen == 0 or blen == 0: return # 어차피 안되는 경우
        flag = 0
        chk = [0] * (N + 1)
        chk[teamA[0]] = 1
        DFS(teamA[0], teamA)
        if flag:
            flag = 0
            chk = [0] * (N + 1)
            chk[teamB[0]] = 1
            table = copy.deepcopy(ori) # 맵 복구
            DFS(teamB[0], teamB)
            if flag:
                # print('다통과')
                # print(teamA)
                # print(teamB)
                # for g in table:
                #     print(g)
                table = copy.deepcopy(ori)  # 맵 복구
                totA, totB = 0, 0
                for a in teamA:
                    totA += people[a-1]
                for b in teamB:
                    totB += people[b-1]
                res = abs(totA - totB)
                # print('res',res)
                if mymin > res:
                    mymin = res
                return
        table = copy.deepcopy(ori)  # 맵 복구
        # print('A',teamA)
        # print('B',teamB)
        # print()
        return
    for i in range(2):
        A[dep] = i
        split(dep + 1)
        A[dep] = 0

N = int(input())
people = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

table = [[0 for _ in range(N+1)] for q in range(N+1)]

for x in range(N):
    for y in range(1, arr[x][0] + 1):
        table[x+1][arr[x][y]] = 1

mymin = 9999999999999
A = [0] * (N+1)
ori = copy.deepcopy(table) # 맵 복사
split(1)
if mymin == 9999999999999:
    print(-1)
else:
    print(mymin)