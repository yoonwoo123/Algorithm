brown = 10
red = 2

def solution(brown, red):
    # 답이 될 수 있는 것은 x, y가 brown + red 의 공약수 이면서
    # (x - 2) * (y - 2) = red를 만족해야 한다.
    # x >= y 이면서 y, x는 최소 3이상이다.
    tot = brown + red
    for y in range(3, tot):
        x = tot // y
        if tot % y == 0 and (x-2) * (y-2) == red:
            return [x, y]


print(solution(brown, red))