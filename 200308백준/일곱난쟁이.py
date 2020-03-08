import sys, itertools
sys.stdin = open("일곱난쟁이_input.txt")

arr = [int(input()) for _ in range(9)]
for comb in itertools.combinations(arr, 7):
    comb = list(comb)
    if sum(comb) == 100:
        comb.sort()
        for n in comb:
            print(n)
        break