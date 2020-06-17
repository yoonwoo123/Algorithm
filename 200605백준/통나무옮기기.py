import sys, collections
sys.stdin = open("통나무옮기기_input.txt")

def BFS():
    global ans
    while q:
        x, y, con, cnt = q.popleft()
        # 중심점을 둘러싼 table 8방향이 전부 0 or B라면 회전 가능
        if x == ex and y == ey and con == fcon:
            ans = cnt
            return
        if is_turn(x, y) and visited[x][y][turn[con]] > cnt + 1:
            q.append([x, y, turn[con], cnt + 1])
            visited[x][y][turn[con]] = cnt + 1
        if con == 'S':
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy
                if dy == 0:
                    # nx 범위를 대조할때는 *2 visit에 넣어줄때는 1
                    if x + dx*2 < 0 or ny < 0 or x + dx*2 >= N or ny >= N or table[x + dx*2][ny] == '1': continue
                    if visited[nx][ny][con] > cnt + 1:
                        q.append([nx, ny, con, cnt + 1])
                        visited[nx][ny][con] = cnt + 1
                else: # 세로방향이므로 x행의 +-1 씩 추가로 범위검증
                    if nx < 0 or nx - 1 < 0 or ny < 0 or nx >= N  or nx + 1 >= N or ny >= N or table[nx][ny] == '1' or table[nx + 1][ny] == '1' or table[nx - 1][ny] == '1': continue
                    if visited[nx][ny][con] > cnt + 1:
                        q.append([nx, ny, con, cnt + 1])
                        visited[nx][ny][con] = cnt + 1

        else:
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy
                if dx == 0:
                    if nx < 0 or y + dy*2 < 0 or nx >= N or y + dy*2 >= N or table[nx][y + dy*2] == '1': continue
                    if visited[nx][ny][con] > cnt + 1:
                        q.append([nx, ny, con, cnt + 1])
                        visited[nx][ny][con] = cnt + 1
                else:
                    if nx < 0 or ny < 0 or ny - 1 < 0 or nx >= N or ny >= N or ny + 1 >= N or table[nx][ny] == '1' or table[nx][ny + 1] == '1' or table[nx][ny - 1] == '1': continue
                    if visited[nx][ny][con] > cnt + 1:
                        q.append([nx, ny, con, cnt + 1])
                        visited[nx][ny][con] = cnt + 1

def is_turn(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N or table[nx][ny] != '0': return False
    return True

N = int(input())
ans = 0
table = []
tree = []
end = []
turn = {'S':'L', 'L': 'S'}
for i in range(N):
    table.append(list(input()))
    for j in range(N):
        if table[i][j] == 'B':
            tree.append([i, j])
            table[i][j] = '0' # 좌표만 저장하고 다 0으로 초기화
        elif table[i][j] == 'E':
            end.append([i, j])
            table[i][j] = '0'

if tree[1][0] == tree[2][0]: # 행이 같다면 누워있는것
    condition = 'L'
else: # 서 있는 것
    condition = 'S'

if end[1][0] == end[2][0]: # 행이 같다면 누워있는것
    fcon = 'L'
else: # 서 있는 것
    fcon = 'S'

visited = [[{'S': 99999, 'L': 99999} for _ in range(N)] for q in range(N)]
sx, sy = tree[1][0], tree[1][1]
ex, ey = end[1][0], end[1][1]
q = collections.deque()
q.append([sx, sy, condition, 0]) # x, y, condition, cnt
visited[sx][sy][condition] = 0
BFS()
print(ans)