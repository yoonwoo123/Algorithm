import sys
sys.setrecursionlimit(10**6)
n = 2000

def solution(n):
    def fibonach(n):
        if data[n] != 0:
            return data[n]
        data[n] = fibonach(n-2) + fibonach(n-1)
        return data[n]

    data = [0 for _ in range(n+1)]
    data[0] = data[1] = 1

    return fibonach(n) % 1234567

print(solution(n))