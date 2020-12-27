import math
w, h = 6, 15

def solution(w,h):
    # w * h = 총개수
    # 총개수 - (큰수/작은수)올림 * 작은수 한 게 답
    minNumber, maxNumber = min(w, h), max(w, h)
    print(maxNumber / minNumber)
    print(math.ceil(maxNumber / minNumber))
    answer = (w * h) - math.ceil(maxNumber / minNumber) * minNumber
    return answer

print(solution(w, h))

def solution1(w,h):
    return w*h - (w+h-math.gcd(w,h))

print(solution1(w, h))