import sys, collections
sys.stdin = open("odd_input.txt")

A = list(map(int, input().split()))
arr = {}
# print(A)
for num in A:
    if num in arr:
    # if arr[num]:
        arr[num] += 1
    else:
        arr[num] = 1

for k, v in arr.items():
    if v % 2 == 1:
        print(k)
