from heapq import heappop, heappush, heapify

jobs = [[0, 3], [1, 9], [2, 6]]

answer = 0
time = 0
wait = []
heapify(wait)
heapify(jobs)
LenJ = len(jobs)
while True:
    while jobs:
        if jobs[0][0] <= time:
            timest, timeva = heappop(jobs)
            heappush(wait, [timeva, timest])
        else:
            break
    if wait == [] and jobs != []: # 디스크가 놀고있을때 jobs가 있다면
        fir = heappop(jobs)
        time += fir[0] - time + fir[1]  # 현재 소요된 시간
        answer += time - fir[0]  # 요청부터 종료까지 걸린 시간
    # print(wait)
    if wait != []:
        v, s = heappop(wait)
        time += v
        answer += time - s
    # print(answer)
    if wait == [] and jobs == []:
        print(answer // LenJ)
        break
