import sys
sys.stdin = open("폰켓몬_input.txt")

nums = list(map(int, input().split()))

answer = 0
N = len(nums)
arr = set(nums)
res = len(arr)
if res >= N//2:
    answer = N//2
else:
    answer = res
print(answer)