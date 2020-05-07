n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    global answer
    answer = 0
    visit = [0] * n

    def DFS(x): # dep = x
        global answer

        if visit[x] == 0:
            visit[x] = 1
            answer += 1

        for y in range(n):
            if x == y: continue
            if computers[x][y]:
                computers[x][y] = computers[y][x] = 0
                visit[y] = 1
                DFS(y)

    for i in range(n):
        if visit[i] == 0:
            DFS(i)
    return answer

print(solution(n, computers))