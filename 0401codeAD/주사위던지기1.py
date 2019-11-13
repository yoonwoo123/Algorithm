import sys, itertools
sys.stdin = open("주사위던지기1_input.txt")
# M1 = 중복순열 구조 :
# M2 = 중복조합 구조 : 조합은 내 앞은 볼 필요 없으므로 start를 들고간다
                     # 그래서 start 부터 시작하면 됨
# M3 = 순열 구조
# M4 가 있다면 조합 구조 : start + 1 부터 시작하면됨

def ovperm(n, k):
    if n == k:
        for g in p:
            print(g, end=" ")
        print()
    else:
        for i in range(k, n):
            p[k] = a[i]
            perm(n, k+1)
            perm(n-1, k+1)
            # a[i], a[k] = a[k], a[i]

def perm(n, k):
    if n == k:
        for g in a:
            print(g, end=" ")
        print()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

N, M = map(int, input().split())
a = [n for n in range(1, 7)]
p = [0] * N

if M == 1:
    permu = itertools.combinations_with_replacement(a, 3)
    for p in permu:
        for i in p:
            print(i, end=" ")
        print()
elif M == 2:
    combi = itertools.combinations_with_replacement(a, 3)
    for c in combi:
        for i in c:
            print(i, end=" ")
        print()
    # ovperm(N, 0)
    # print(1)


elif M == 3:
    combi = itertools.combinations(a, 3)
    for c in combi:
        for i in c:
            print(i, end=" ")
        print()

