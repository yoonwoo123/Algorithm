import sys, itertools
sys.stdin = open("블랙잭_input.txt")

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
combs = list(itertools.combinations(cards, 3))
for comb in combs:
    tot = sum(comb)
    if tot > M: continue
    if tot == M:
        ans = tot
        break
    if ans < tot:
        ans = tot
print(ans)