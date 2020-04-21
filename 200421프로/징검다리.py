import sys, math
sys.stdin = open("징검다리_input.txt")

distance, n = map(int, input().split())
rocks = list(map(int, input().split()))

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        prev = 0
        my_min = math.inf
        removed_rocks = 0
        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed_rocks += 1
            else:
                my_min = min(my_min, rocks[i] - prev)
                prev = rocks[i]

        if removed_rocks > n:
            right = mid - 1
        else:
            answer = my_min
            left = mid + 1
    return answer

print(solution(distance, rocks, n))