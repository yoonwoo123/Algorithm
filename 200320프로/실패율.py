import sys
sys.stdin = open("실패율_input.txt")
input = sys.stdin.readline

N = int(input())
stages = list(map(int, input().split()))

answer = []
arr = [0] * (N + 2)
for num in stages:
    arr[num] += 1

cnt = len(stages)
fper = []
for i in range(1, N+1):
    if arr[i] == 0:
        fper.append([0, i])
    else:
        fper.append([arr[i] / cnt, i])
        cnt -= arr[i]

fper = sorted(fper, reverse=True, key=lambda x:x[0])
for per, idx in fper:
    answer.append(idx)
print(answer)

# result = {}
# denominator = len(stages)
# for stage in range(1, N+1):
#     if denominator != 0:
#         count = stages.count(stage)
#         result[stage] = count / denominator
#         denominator -= count
#     else:
#         result[stage] = 0
#
# print(sorted(result, key=lambda x : result[x], reverse=True))
