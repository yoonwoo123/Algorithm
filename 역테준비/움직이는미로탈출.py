import sys, collections
sys.stdin = open("움직이는미로탈출_input.txt")
input = sys.stdin.readline

# 욱제는 7, 0 에서 시작, 목표지점은 0, 7이다.

def BFS():
    q = collections.deque()
    q.append((7, 0))

    while q:
        visited = [[0 for _ in range(8)] for _ in range(8)]
        # 욱제 1칸 이동
        for _ in range(len(q)):
            x, y = q.popleft()
            # 벽이 욱제와 만났으니 종료
            if table[x][y] == '#': continue
            for i in range(9):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= 8 or ny >= 8 or table[nx][ny] == '#' or visited[nx][ny]: continue
                if nx == 0 and ny == 7: return 1

                q.append((nx, ny))
                visited[nx][ny] = 1

        # 벽 밑으로 1칸 이동
        down()

    return 0

def down():
    for j in range(8):
        for i in range(7, 0, -1):
            table[i][j] = table[i-1][j]
        table[0][j] = '.'

dx = (-1, -1, 0, 1, 1, 1, 0, -1, 0)
dy = (0, 1, 1, 1, 0, -1, -1, -1, 0)

table = [list(input()) for _ in range(8)]
print(BFS())