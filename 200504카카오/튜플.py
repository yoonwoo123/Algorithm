s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

def solution(s):
    answer = []
    splits = []
    for string in s.split('{'):
        tmp = ''
        s = []
        for char in string:
            if char.isdecimal():
                tmp += char
            else:
                if tmp != '':
                    s.append(int(tmp))
                    tmp = ''
        if s != []:
            splits.append(s)
    # 나온 횟수가 큰만큼 먼저나온것이므로 횟수 내림차순으로 정렬하자.
    nums = {}
    for spl in splits:
        for num in spl:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
    return sorted(nums.keys(), reverse=True, key= lambda x:nums[x])

print(solution(s))