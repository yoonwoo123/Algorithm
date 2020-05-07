stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
def solution(stones, k):
    answer = 0
    left = min(stones)
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        flag = True
        for i in range(len(stones)):
            if mid > stones[i]:
                cnt += 1
                if cnt >= k:
                    flag = False
                    break
            else:
                cnt = 0
        if flag:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(solution(stones, k))