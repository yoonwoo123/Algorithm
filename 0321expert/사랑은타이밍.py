import sys
sys.stdin = open("사랑은타이밍_input.txt")

tc = int(input())
for T in range(1, tc+1):
    total = 0
    D, H, M = map(int, input().split())
    total += D*24*60 + H*60 + M - 16511
    if total < 0:
        print('#{} {}'.format(T, -1))
    else:
        print('#{} {}'.format(T, total))