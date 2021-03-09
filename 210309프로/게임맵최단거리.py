import collections

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution(maps):
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    h, w = len(maps), len(maps[0])

    def BFS():
        visited = [[0 for _ in range(w)] for q in range(h)]
        q = collections.deque()
        q.append((0, 0, 1))
        visited[0][0] = 1

        while q:
            x, y, cnt = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= h or ny >= w or maps[nx][ny] == 0 or visited[nx][ny]: continue
                visited[nx][ny] = 1
                if nx == h - 1 and ny == w - 1: return cnt + 1
                q.append((nx, ny, cnt + 1))

        return -1

    return BFS()

print(solution(maps))