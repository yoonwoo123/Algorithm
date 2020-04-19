import sys
sys.stdin = open("무지의먹방라이브_input.txt")

food_times = list(map(int, input().split()))
k = int(input())

s_ftimes = sorted(food_times)
fsum = sum(food_times)
L = len(food_times)
if k >= fsum:
    print(-1)
else:
    chk = 0
    for i in range(L):
        m = s_ftimes[i]
        if k > (m - chk) * (L - i):
            k -= (m - chk) * (L - i)
            chk = m
        else:
            k %= L - i
            break
    k += 1
    i = 0
    while True:
        i %= L
        if food_times[i] > chk:
            k -= 1
            if k == 0:
                print(i + 1)
                break
        i += 1
