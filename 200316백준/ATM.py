import sys
sys.stdin = open("ATM_input.txt")

N = int(input())
P = list(map(int, input().split()))
P.sort()
tot, ans = 0, 0
for i in range(N):
    tot += P[i]
    ans += tot
print(ans)