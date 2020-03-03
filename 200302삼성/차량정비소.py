import sys
sys.stdin = open("차량정비소_input.txt")
input = sys.stdin.readline

tc = int(input())
for T in range(1, tc + 1):
    N, M, K, A, B = map(int, input().split())
    recepts = list(map(int, input().split()))
    repairs = list(map(int, input().split()))
    customers = list(map(int, input().split()))  # 고객의 번호는 1부터 시작
                                                 # 시간은 0초부터 시작
    visits = [[0, 0] for _ in range(K + 1)]  # 청구, 수리 방문한 위치 표시
    recepting = [[0, 0] for _ in range(N)]  # 방문한 손님번호, recepts[i]
    repairing = [[0, 0] for _ in range(M)]
    waitA = []
    waitB = []
    times = {}
    for i in range(K):
        if customers[i] in times:
            times[customers[i]].append(i + 1)
        else:
            times[customers[i]] = [i + 1]
    t = 0
    while K:
        if t in times:
            waitA.extend(times[t])

        for n in range(N):
            if recepting[n][0] == 0 and waitA:
                cusnum = waitA.pop(0)
                recepting[n][0] = cusnum
                recepting[n][1] = recepts[n]
                visits[cusnum][0] = n + 1
        for n in range(N):
            if recepting[n][0]:  # 손님이 있으면
                recepting[n][1] -= 1
                if recepting[n][1] == 0:
                    waitB.append(recepting[n][0])
                    recepting[n][0] = 0  # 손님이 없다고 표시

        for m in range(M):
            if repairing[m][0] == 0 and waitB:
                cusnum = waitB.pop(0)
                repairing[m][0] = cusnum
                repairing[m][1] = repairs[m]
                visits[cusnum][1] = m + 1

        for m in range(M):
            if repairing[m][0]:
                repairing[m][1] -= 1
                if repairing[m][1] == 0:
                    repairing[m][0] = 0
                    K -= 1
        t += 1
    ans = 0
    for i in range(1, len(visits)):
        if visits[i][0] == A and visits[i][1] == B:
            ans += i
    if ans == 0:
        ans = -1
    print(f"#{T} {ans}")