import sys
sys.stdin = open("신입사원_input.txt")
input = sys.stdin.readline

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    scores = [0] * (N+1)
    for _ in range(N):
        a, b = map(int, input().split())
        scores[a] = b
    ans = 1
    cand = scores[1]
    for i in range(2, N+1):
        if cand == 1: break
        if cand > scores[i]:
            cand = scores[i]
            ans += 1
    print(ans)