import sys
sys.stdin = open("미로2_input.txt")

dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
dy = [0, 1, 0, -1]

def bfs(x, y):
    q.append([x, y])
    maze[y][x] = 9
    while len(q) != 0:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if maze[ny][nx] == 0:
                q.append([nx, ny])
                maze[ny][nx] = 9
                continue
            elif maze[ny][nx] == 3:
                return 1
    return 0

for T in range(1, 11):
    tc = input()
    maze = []
    q = []
    for i in range(100):
        maze.append(list(map(int, list(input()))))
    print("%s%d %d" % ('#', T, bfs(1, 1)))