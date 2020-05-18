import sys, math
sys.stdin = open("숫자만들기_input.txt")

def DFS(dep, tot):
    global max_num, min_num
    if dep == len(nums) - 1:
        max_num = max(max_num, tot)
        min_num = min(min_num, tot)
        return

    for i in range(4):
        if opers[i] == 0: continue
        opers[i] -= 1
        DFS(dep + 1, operator(tot, nums[dep + 1], i))
        opers[i] += 1

def operator(tot, num, oper):
    if oper == 0:
        return tot + num
    elif oper == 1:
        return tot - num
    elif oper == 2:
        return tot * num
    else:
        if tot < 0:
            return -(-tot // num)
        return tot // num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    opers = list(map(int, input().split())) # + - * /
    nums = list(map(int, input().split()))
    max_num = -math.inf
    min_num = math.inf
    DFS(0, nums[0])
    print(f'#{tc} {max_num - min_num}')