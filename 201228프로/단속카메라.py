routes = [[-20, 15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort()
    i = 0
    endA = routes[i][1]
    startB, endB = routes[i + 1]

    while i < len(routes):
        if endA < startB:
            answer += 1
            i += 1
            if i >= len(routes) - 1:
                answer += 1
                break
            endA = endB
            startB, endB = routes[i+1]
            continue

        endA = min(endA, endB)
        i += 1
        if i >= len(routes) - 1:
            answer += 1
            break
        startB, endB = routes[i+1]

    return answer

print(solution(routes))