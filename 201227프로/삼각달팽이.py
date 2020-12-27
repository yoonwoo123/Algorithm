n = 6

def solution(n):
    answer = []
    dx = (1, 0, -1)
    dy = (0, 1, -1)
    triangle = [[0 for _ in range(x)] for x in range(1, n+1)]

    number, dir, count = 1, 0, 0
    x, y = 0, 0
    triangle[x][y] = number

    while count < 2:
        nx, ny = x + dx[dir], y + dy[dir]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or triangle[nx][ny]:
            dir = (dir + 1) % 3
            count += 1
        else:
            number += 1
            triangle[nx][ny] = number
            x, y = nx, ny
            count = 0

    for row in triangle:
        answer.extend(row)

    return answer

print(solution(n))