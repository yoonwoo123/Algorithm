import sys, itertools, copy
sys.stdin = open("게리맨더링_input.txt")

def check(team):
    global flag
    flag = False
    if len(team) == 1: return True
    # 들어간 행과 팀, 체크배열
    chk = [0 for _ in range(N + 1)]
    chk[team[0]] = 1
    # sum(체크배열)의 값이 len(team)과 같으면 True
    DFS(team[0], team, chk)
    return flag

def DFS(x, team, chk):
    global flag
    if sum(chk) == len(team):
        flag = True
        return

    for y in range(1, N + 1):
        if table[x][y] and chk[y] == 0 and y in team:
            table[x][y] = table[y][x] = 0
            chk[y] = 1
            DFS(y, team, chk)
            table[x][y] = table[y][x] = 1

N = int(input())
peoples = list(map(int, input().split()))
ans = 999999 # 최소값

table = [[0 for _ in range(N+1)] for q in range(N+1)] # idx 때문에 +1
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for x in range(1, len(tmp)):
        table[i][tmp[x]] = 1

for i in range(1, N//2 + 1):
    for comb in itertools.combinations([x for x in range(1, N+1)], i):
        teamA = set(comb)
        teamB = set(x for x in range(1, N+1)) - teamA
        if check(list(teamA)) and check(list(teamB)):
            A = B = 0
            for num in teamA:
                A += peoples[num-1]
            for num in teamB:
                B += peoples[num-1]
            ans = min(ans, abs(A-B))
if ans == 999999:
    print(-1)
else:
    print(ans)

# def BFS(team):
#     if len(team) == 1: return True
#     q = []
#     q.append(team[0])
#     visited = [0 for _ in range(N+1)]
#     visited[team[0]] = 1
#     while q:
#         x = q.pop()
#         for y in range(1, N + 1):
#             if table[x][y] and visited[y] == 0 and y in team:
#                 table[x][y] = table[y][x] = 0
#                 visited[y] = 1
#                 q.append(y)
#     if sum(visited) == len(team): return True
#     return False
#
# N = int(input())
# peoples = list(map(int, input().split()))
# ans = 999999 # 최소값
#
# table = [[0 for _ in range(N+1)] for q in range(N+1)] # idx 때문에 +1
# for i in range(1, N+1):
#     tmp = list(map(int, input().split()))
#     for x in range(1, len(tmp)):
#         table[i][tmp[x]] = 1
# ori = copy.deepcopy(table)
#
# for i in range(1, N//2 + 1):
#     for comb in itertools.combinations([x for x in range(1, N+1)], i):
#         teamA = set(comb)
#         teamB = set(x for x in range(1, N+1)) - teamA
#         if BFS(list(teamA)) and BFS(list(teamB)):
#             A = B = 0
#             for num in teamA:
#                 A += peoples[num-1]
#             for num in teamB:
#                 B += peoples[num-1]
#             ans = min(ans, abs(A-B))
#         table = copy.deepcopy(ori)
# if ans == 999999:
#     print(-1)
# else:
#     print(ans)