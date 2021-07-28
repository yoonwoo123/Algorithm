rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    def rotate(query):
        # x1, y1, x2, y2 가 들어온다면
        # 회전알고리즘은 x1, y1 에서 x1, y2까지 진행한후
        # x1, y2 -> x2, y2까지 진행하고
        # x2, y2 -> x2, y1
        # x2, y1 -> x1, y1 이 순서로 좌표값을 옮긴다.
        # 그 전 좌표값이 0이 아니라면 그 수로 바꿔주고 (바꾸기전 그전좌표값에 저장)
        # 0이라면 (바꾸기전 그전좌표값 저장)현재좌표값을 넣는다
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        beforeValue = 0
        x, y = x1, y1
        minValue = table[x][y]

        for i in range(4):
            while True:
                nx, ny = x + dx[i], y + dy[i]

                if nx < x1 or nx > x2 or ny < y1 or ny > y2: break
                minValue = min(minValue, table[nx][ny])

                if beforeValue:
                    table[nx][ny], beforeValue = beforeValue, table[nx][ny]

                else:
                    beforeValue = table[nx][ny]
                    table[nx][ny] = table[x][y]

                x, y = nx, ny

        return minValue

    answer = []
    table = [[y + x * columns for y in range(1, columns + 1)] for x in range(rows)]

    for query in queries:
        answer.append(rotate(query))

    return answer

print(solution(rows, columns, queries))