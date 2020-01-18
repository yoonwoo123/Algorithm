import sys, heapq
sys.stdin = open("예산_input.txt")

budgets = list(map(int, input().split()))
M = int(input())

answer = 0
LenB = len(budgets)
SumB = sum(budgets)
MaxB = max(budgets)
if SumB <= M:
    answer = MaxB

else:
    left = M // LenB
    right = MaxB
    while left <= right:
        mid = (left + right) // 2
        tot = 0
        for budget in budgets:
            if budget <= mid:
               tot += budget
            else:
                tot += mid
        if tot <= M:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
print(answer)