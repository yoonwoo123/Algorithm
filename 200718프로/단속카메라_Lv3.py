routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort()
    print(routes)
    # 정렬을 한 다음에 회의 시간을 잡는 문제처럼 시작시간과 끝나는 시간 비교처럼
    # 시작 지점과 끝나는 지점을 잘 비교하면 될 것 같다.
    return answer

print(solution(routes))