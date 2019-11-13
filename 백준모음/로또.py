import sys
sys.stdin = open("로또_input.txt")

def DFS(cnt, s):
    if cnt == 6:
        print(" ".join(tmp))
        return

    for i in range(s, K):
        tmp.append(nums[i])
        DFS(cnt + 1, i+1)
        tmp.pop()

nums = list(input().split())
while True:
    K = int(nums.pop(0)) # nums 의 개수
    tmp = []
    DFS(0, 0)
    nums = list(input().split())
    if nums[0] == '0': break
    print()
