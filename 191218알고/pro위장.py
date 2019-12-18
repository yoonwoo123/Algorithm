import sys
sys.stdin = open("위장_input.txt")

tmp = list(input().split())
LT = len(tmp)
clothes = []
for i in range(0, LT//2):
    clothes.append([tmp[i*2], tmp[i*2+1]])

answer = 1
spy = {}
for clothe in clothes:
    if clothe[1] in spy:
        spy[clothe[1]] += 1
    else:
        spy[clothe[1]] = 1

arr = list(spy.values())

for num in arr:
    answer *= num + 1

print(answer-1)

