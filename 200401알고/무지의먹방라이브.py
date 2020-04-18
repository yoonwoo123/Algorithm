import sys
sys.stdin = open("무지의먹방라이브_input.txt")

food_times = list(map(int, input().split()))
k = int(input())

s_ftimes = sorted(food_times)
print(s_ftimes)
fsum = sum(food_times)
L = len(food_times)
if k >= fsum:
    print(-1)
else:
    chk = 0
    for i in range(L):
        print(k)
        m = s_ftimes[i]
        if k > (m - chk) * (L - i):
            k -= (m - chk) * (L - i)
            chk = m
        else:
            break
    k %= L
    cnt = k
    i = 0
    while True:
        if food_times[i] <= chk:
            i += 1
        else:
            cnt -= 1
            if cnt == 0:
                aa = i + 1
                break
    aa %= L
    print(aa)
    while food_times[aa] <= chk:
        aa = (aa + 1) % L

    print(aa+1)
