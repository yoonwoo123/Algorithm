import sys
sys.stdin = open('sw02_백만장자_input.txt')

testcases = int(input())
for T in range(testcases):
    N = int(input())

    nums = list(map(int,(input().split())))
    nums = nums[::-1]
    max = 0
    total = 0
    idx = []
    result = []
    for i in range(len(nums)): # max의 idx 찾기
        if max < nums[i]:
            max = nums[i]
            idx.append(i)
    idx = idx[::-1]
    # print(idx)
    for i in range(idx[0]+1, len(nums)): # max1 전값까지 전부 더하기
        total += nums[i]
    result.append(nums[idx[0]] * (len(nums)-idx[0]-1) - total)
    total = 0
    if len(idx) > 1:
        for x in range(len(idx)-1):
            total = 0
            for i in range(idx[x+1]+1, idx[x]):
                total += nums[i]
            result.append(nums[idx[x+1]] * (idx[x]-idx[x+1]-1) - total)
    print(f'#{T+1} {sum(result)}')