import sys
sys.stdin = open("미로2_input.txt")

def bfs(x, y):
    global flag
    cnt = 0
    maze[y][x] = 9  # 방문표시
    while flag != 1:
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
    old = []
    for i in range(100):
        maze.append(list(map(int, list(input()))))
    print("%s%d %d" % ('#', T + 1, bfs(1, 1)))