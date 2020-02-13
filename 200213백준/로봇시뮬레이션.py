import sys, itertools
sys.stdin = open("로봇시뮬레이션_input.txt")
input = sys.stdin.readline

def sol():
    for i in range(M):
        n, com, cnt = input().strip().split()
        n, cnt = int(n) - 1, int(cnt)
        x, y, dir = robots[n]
        if com == 'L':
            for q in range(cnt % 4):
                robots[n][2] = turns[0][dir]
                dir = robots[n][2]
        elif com == 'R':
            for q in range(cnt % 4):
                robots[n][2] = turns[1][dir]
                dir = robots[n][2]
        else:  # F 였을 경우
            for q in range(cnt):
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or ny < 0 or nx >= B or ny >= A:
                    print(f'Robot {n+1} crashes into the wall')
                    return
                if table[nx][ny]:
                    print(f'Robot {n+1} crashes into robot {table[nx][ny]}')
                    return
                table[nx][ny], table[x][y] = n+1, 0
                robots[n][0], robots[n][1] = nx, ny
                x, y = nx, ny
    print('OK')
A, B = map(int, input().split()) # 열, 행
table = [[0 for q in range(A)] for _ in range(B)]
N, M = map(int, input().split())           # L= 0, R = 1
turns = ((2, 3, 1, 0), (3, 2, 0, 1)) # dir = turns[0][dir]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
robots = []
for i in range(N):
    y, x, dir = input().strip().split()
    x, y = int(x) - 1, int(y) - 1
    # 동서남북 = dir 0123 으로 저장
    if dir == 'E':
        robots.append([x, y, 0])
    elif dir == 'W':
        robots.append([x, y, 1])
    elif dir == 'N': # 남북이 바뀜 배열은 좌측최상단이 0,0이므로
        robots.append([x, y, 2])
    else:
        robots.append([x, y, 3])
    table[x][y] = i+1
sol()


