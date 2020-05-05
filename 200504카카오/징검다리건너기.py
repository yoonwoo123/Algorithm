
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

def solution(stones, k):
    left = min(stones)
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        flag = True
        for stone in stones:
            if mid > stone:
                cnt += 1
                if cnt >= k:
                    flag = False
                    break
            else:
                cnt = 0
        if flag: # 통과할 수 있으며 더 커질 가능성있다.
            left = mid + 1
        else:
            right = mid - 1
    return right

print(solution(stones, k))