import sys
sys.stdin = open("미로_input.txt")
dx = [1, 0, -1, 0] # 우, 하, 좌, 상
dy = [0, 1, 0, -1]

def dfs(x, y):
    cnt = 0
    while len(flag) == 0:
        maze[y][x] = 9  # 방문표시
        if 0 <= x + dx[cnt] < N and 0 <= y + dy[cnt] < N:
            nx = x + dx[cnt]
            ny = y + dy[cnt]
        else:
            cnt += 1
            if cnt > 3:
                break
            continue
        # nx = x + dx[cnt]
        # ny = y + dy[cnt]
        if maze[ny][nx] == 3:
            flag.append(1)
            break
        if maze[ny][nx] == 0: # 함수를 넣어서 갈 수 있는 것만 통과
            old.append(cnt)
            y = ny
            x = nx
            cnt = 0
            continue
        nx = 0
        ny = 0
        cnt += 1
        if cnt > 3 and len(old) > 0 :
            p = old.pop()
            if p == 99:
                break
            x = x - dx[p]
            y = y - dy[p]
            cnt = 0
            continue

    if len(flag) > 0:
        return 1
    return 0

testcases = int(input())
for T in range(testcases):
    N = int(input())
    maze = []
    flag = []
    old = [99]
    for i in range(N):
        tmp = []
        for num in input():
            tmp.append(int(num))
        maze.append(tmp)
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                s_y = y
                s_x = x
                break
    print(f'#{T+1} {dfs(s_x, s_y)}')
    # 출발점은 1,1 로 동일하고 가로는 x 세로는 y다.
    # 도착점은 3이며 통로는 0이다. 도착점을 찾지못하며 0반환 찾으면 1반환
    # 방문한 곳은 9를 넣어 방문표시를 하고 더이상 진행할수 없으면 진행할수있는 상태로 되돌아가야한다.
    # 시작점에서 상하좌우를 확인하여 '0' 인곳을 찾아 이동한다.
    # 상하좌우에 '0'이 없으면 그 전상황으로 돌아간다
    # 모든 상황에 '0'이 없으면 최종적으로 0을 반환한다.
