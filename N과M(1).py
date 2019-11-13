import sys, itertools
sys.stdin = open("NM1_input.txt")

N, M = map(int, input().split())

a = [x for x in range(1, N+1)]
perm = list(itertools.permutations(a, M))
for per in perm:
    for i in range(M):
        print(per[i], end=" ")
    print()