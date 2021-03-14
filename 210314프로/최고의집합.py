n = 171
s = 2743

def solution(n, s):
    if n > s:
        return [-1]

    q = s // n
    r = s % n

    answer = [q for _ in range(n)]

    for i in range(n-1, n-r-1, -1):
        answer[i] += 1

    return answer

print(solution(n, s))