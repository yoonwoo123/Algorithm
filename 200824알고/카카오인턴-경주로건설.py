import collections

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def solution(board):
    def BFS():
        q = collections.deque()
        q.append([0, 0, 1]) # x, y, dir, tot
        q.append([0, 0, 3])
        for x in range(4):
            memo[0][0][x] = 0
        while q:
            x, y, dir = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board) or board[nx][ny]: continue
                if dir == i and memo[nx][ny][i] > memo[x][y][dir] + 100: # 방향이 일치 100만 소모
                    memo[nx][ny][i] = memo[x][y][dir] + 100
                    q.append([nx, ny, i])
                elif dir != i and memo[nx][ny][i] > memo[x][y][dir] + 600:
                    memo[nx][ny][i] = memo[x][y][dir] + 600
                    q.append([nx, ny, i])

    answer = 0
    memo = [[[99999999 for w in range(4)] for _ in range(len(board))] for q in range(len(board))]
    BFS()
    answer = min(memo[len(board)-1][len(board)-1])
    return answer

print(solution(board))