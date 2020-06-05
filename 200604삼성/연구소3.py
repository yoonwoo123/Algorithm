import sys, itertools, collections
sys.stdin = open("연구소3_input.txt")

def BFS(comb):
    global ans
    visited = [[9999 for _ in range(N)] for q in range(N)]
    q = collections.deque()
    for x, y in comb:
        q.append([x, y])
        visited[x][y] = 0
    # 시간으로 표시하자. 시간이 작거나 같으면 q에 추가하지 않아도됨
    cnt = 0 # 빈칸을 오염시킨 횟수
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] == 1: continue
            if table[nx][ny] == 0:
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt += 1
                    if cnt == blanks:
                        ans = min(ans, visited[nx][ny])
                        return
                    q.append([nx, ny])
            elif table[nx][ny] == 2:
                if visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])


N, M = map(int, input().split())
table = []
viruses = []
blanks = 0 # 빈 칸의 개수들 나중에 바이러스가 전부 퍼졌는지 비교
for i in range(N):
    table.append(list(map(int, input().split())))
    for j in range(N):
        if table[i][j] == 2: # 바이러스
            viruses.append([i, j])
        elif table[i][j] == 0: # 빈칸의 개수를 미리 세두자
            blanks += 1


# 바이러스의 좌표들을 구한 후 조합으로 좌표들중 M개를 뽑는다.
# 그 바이러스들을 BFS로 맵에 퍼트리면서 최소시간을 구하자.
if blanks == 0:
    print(0)
else:
    ans = 999999 # 최소값을 구해야한다.
    for comb in itertools.combinations(viruses, M):
        BFS(comb)
    if ans == 999999:
        print(-1)
    else:
        print(ans)