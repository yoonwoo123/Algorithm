import sys, copy
sys.stdin = open("화물도크_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    sche = []
    for i in range(N):
        S, E = map(int, input().split())
        sche.append([E, S])
    sche.sort()
    tmp = 0
    cnt = 0
    for i in range(N):
        if tmp <= sche[i][1]:
            tmp = sche[i][0]
            cnt += 1
    print('#%d %d' % (T, cnt))