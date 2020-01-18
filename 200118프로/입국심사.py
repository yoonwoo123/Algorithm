import sys, heapq
sys.stdin = open("입국심사_input.txt")

n = int(input())
times = list(map(int, input().split()))

answer = 0
times.sort()
LenT = len(times)
left = times[0] * n // LenT
right = times[-1] * n // LenT
while left <= right:
    mid = (left + right) // 2
    tot = 0
    for time in times:
        tot += mid // time
    if tot >= n:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)