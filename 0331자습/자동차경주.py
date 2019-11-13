import sys, collections
sys.stdin = open("자동차경주_input.txt")

limit = int(input())
N = int(input())
meter = list(map(int, input().split()))
totmeter = sum(meter)
time = list(map(int, input().split()))
metime = []
for i in range(N):
    metime.append([meter[i], time[i]])
print(metime)

if metime[i] <= limit:
    