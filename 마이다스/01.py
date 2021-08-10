N = 9
mine = [[1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6]]

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

def solution(N, mine):
    def setMines():
        for x, y in mine:
            board[x - 1][y - 1] = -1

    def countNearMine():
        for x in range(N):
            for y in range(N):
                if board[x][y] != -1:
                    mineCount = 0

                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                        if board[nx][ny] == -1:
                            mineCount += 1

                    board[x][y] = mineCount

    board = [[0 for _ in range(N)] for q in range(N)]

    setMines()
    countNearMine()

    return board

print(solution(N, mine))