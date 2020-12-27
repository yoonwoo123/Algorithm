from math import gcd

def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while len(arr) > 1:
        arr.append(lcm(arr.pop(), arr.pop()))

    return arr[0]

print(solution([1, 2, 3]))