import sys, collections
sys.stdin = open("minsearch_input.txt")

A = list(map(int, input().split()))

chk = [0] * 100002 # 0 ~ 100001 까지
for num in A:
    if 0 < num <= 100000:
        chk[num] = 1

for i in range(1, 100002):
    if chk[i] == 0:
        print(i)
        break