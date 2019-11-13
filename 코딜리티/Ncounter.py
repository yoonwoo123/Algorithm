import sys, collections
sys.stdin = open("Ncounter_input.txt")

N = int(input())
A = list(map(int, input().split()))

res = [0] * N
mymax = 0 # 그 배열 중 최댓값 계속 갱신
mcount = 0
for num in A:
    if 1 <= num <= N:
        if res[num - 1] < mcount:
            res[num - 1] = mcount + 1
            if mymax < mcount + 1:
                mymax = mcount + 1
        else:
            res[num - 1] += 1
            if mymax < res[num - 1]:
                mymax = res[num - 1]

    elif num == N + 1:
        mcount = mymax

for i in range(N):
    if res[i] < mcount:
        res[i] = mcount

print(res)