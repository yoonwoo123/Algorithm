import collections

places = [["PXPOO", "XXOOO", "PXOOO", "OPOOO", "OOPOX"]]

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def solution(places):
    def BFS(sx, sy):
        q = collections.deque()
        q.append((sx, sy, 0))
        visited = [[0 for _ in range(len(place))] for q in range(len(place))]

        while q:
            x, y, cnt = q.popleft()
            visited[x][y] = 1

            if cnt == 2: break

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= len(place) or ny < 0 or ny >= len(place) or place[nx][ny] == 'X' or visited[nx][ny]: continue
                if place[nx][ny] == 'P':
                    return 0

                q.append((nx, ny, cnt + 1))

        return 1

    answer = []

    for place in places:
        candidates = []

        for x in range(len(place)):
            for y in range(len(place)):
                if place[x][y] == "P":
                    candidates.append((x, y))

        success = 1
        for sx, sy in candidates:
            if BFS(sx, sy) == 0:
                success = 0
                break

        answer.append(success)

    return answer

print(solution(places))