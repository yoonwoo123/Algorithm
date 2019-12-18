import sys
sys.stdin = open("전화번호목록_input.txt")

def solution(phone_book):
    nums = {}
    for phonenum in phone_book:
        if phonenum[0] in nums:
            nums[phonenum[0]].append(phonenum)
        else:
            nums[phonenum[0]] = [phonenum]
    # print(nums)
    # print(nums['1'][0][0:3])
    for n in nums:
        LN = len(nums[n])
        if LN > 1:
            for i in range(LN-1):
                LI = len(nums[n][i])
                for j in range(i+1, LN):
                    LJ = len(nums[n][j])
                    if LI < LJ:
                        if nums[n][i] == nums[n][j][0:LI]:
                            return False
                    else:
                        if nums[n][j] == nums[n][i][0:LJ]:
                            return False
    return True

phone_book = list(map(str, input().split()))
answer = True

print(solution(phone_book))