import sys, collections
sys.stdin = open("보물섬_input.txt")

def island_num():
    ans = 0
    for x in range(R):
        for y in range(C):
            if table[x][y] == 'L':
                if y + 1 < C and y - 1 >= 0 and table[x][y+1] == 'L' and table[x][y-1] == 'L': continue
                if x + 1 < R and x - 1 >= 0 and table[x+1][y] == 'L' and table[x-1][y] == 'L': continue
                ans = max(ans, BFS(x, y))
    return ans

def BFS(x, y):
    q.append([x, y, 0])
    visited = {(x, y):1}
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C or table[nx][ny] == 'W' or (nx, ny) in visited: continue
            visited[(nx, ny)] = 1
            q.append([nx, ny, cnt + 1])
    return cnt

R, C = map(int, input().split())
table = [list(input().strip()) for _ in range(R)]
q = collections.deque()
print(island_num())