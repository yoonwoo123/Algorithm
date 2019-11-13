import sys
sys.stdin = open("미로1_input.txt")

dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
dy = [0, 1, 0, -1]


def dfs(x, y):
    maze[y][x] = 9  # 방문표시

    for i in range(4):
        global flag
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[ny][nx] == 3:
            flag = 1
            break
        if maze[ny][nx] == 0:  # 함수를 넣어서 갈 수 있는 것만 통과
            dfs(nx, ny)
    if flag == 1:
        return 1
    else:
        return 0

testcases = 10
for T in range(testcases):
    tc = input()
    maze = []
    flag = 0
    for i in range(16):
        maze.append(list(map(int, list(input()))))
    dfs(1, 1)
    print("%s%d %d" % ('#', T + 1, flag))