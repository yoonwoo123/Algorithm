def sumThr():
    global ans
    start = N // 5
    for i in range(start, 0, -1):
        cnt = i
        tmp = i*5
        while True:
            tmp += 3
            cnt += 1
            if tmp > N:
                break
            elif tmp == N:
                ans = cnt
                return

N = int(input())
# 3의 배수, 5의 배수인 것들인지 확인해서 그 몫을 기록해준다.
ans = 9999
if N % 3 == 0:
    if ans > N // 3:
        ans = N // 3
if N % 5 == 0:
    if ans > N // 5:
        ans = N // 5
else:
    sumThr()

if ans == 9999:
    print(-1)
else:
    print(ans)