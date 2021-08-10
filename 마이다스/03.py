N = 4
K = 4
T = [[1,3],[1,1],[2,3],[3,4]]
# greedy 하게 정렬로 b가 낮은 순, a가 낮은 순 으로 정렬해보자.
# answer는 최대값을 반환하는데 K랑 같아진다면 바로 return하여 끝내도 된다.

def solution(N, K, T):
    def makeSchedules():
        for i in range(1, len(T) + 1):
            start, end = T[i - 1]
            for day in range(start - 1, end):
                schedules[day].append(i)

    def meetStudent():
        meetCount = 0

        for schedule in schedules:
            for student in schedule:
                if isMeet[student] == 0:
                    isMeet[student] = 1
                    meetCount += 1
                    break

        return meetCount

    T.sort(key=lambda x: (x[1], x[0]))
    schedules = [[] for _ in range(K)]
    isMeet = {x: 0 for x in range(1, N + 1)}

    makeSchedules()
    answer = meetStudent()

    return answer


print(solution(N, K, T))