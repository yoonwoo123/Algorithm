import sys, itertools
sys.stdin = open("요리사_input.txt")

tc = int(input())
for T in range(1, tc + 1):
    N = int(input())
    synergys = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999
    for comb in itertools.combinations(range(N), N//2):
        candidates = [q for q in range(N)]
        for n in comb:
            candidates.remove(n)
        A = 0
        for x in range(N//2 - 1):
            for y in range(x+1, N//2):
                sx, sy = comb[x], comb[y]
                A += synergys[sx][sy] + synergys[sy][sx]
        B = 0
        for x in range(N // 2 - 1):
            for y in range(x + 1, N // 2):
                sx, sy = candidates[x], candidates[y]
                B += synergys[sx][sy] + synergys[sy][sx]
        ans = min(ans, abs(A-B))
    print('#{} {}'.format(T, ans))