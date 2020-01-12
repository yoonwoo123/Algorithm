import sys, heapq
sys.stdin = open("더맵게_input.txt")

scoville = list(map(int, input().split()))
K = int(input())

answer = 0
heapq.heapify(scoville)
heapq.heappush(scoville, 1000000001)
while True:
    fir = heapq.heappop(scoville)
    if fir >= K:
        print(answer)
        break
    answer += 1
    sec = heapq.heappop(scoville)
    if sec == 1000000001:
        answer = -1
        print(answer)
        break
    new = fir + sec * 2
    heapq.heappush(scoville, new)
