tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

def solution(tickets):
    global answer
    answer = ['ZZZ']  # 답이 될 수 있는 후보들을 모은 후 sort 후 0번째것이 답
    def DFS(dep, schedule):
        global answer
        if dep == len(tickets) - 1:
            answer = min(answer, schedule)[:]
            return

        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[i][0] == schedule[-1]:
                visited[i] = 1
                schedule.append(tickets[i][1])
                DFS(dep + 1, schedule)
                schedule.pop()
                visited[i] = 0

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            schedule = tickets[i]
            visited = [0 for _ in range(len(tickets))]
            visited[i] = 1
            DFS(0, schedule)
    return answer

print(solution(tickets))