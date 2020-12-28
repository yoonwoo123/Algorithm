a = [-16,27,65,-2,58,-92,-71,-68, -80, -61, -43, -70, -43, -72, -33]

def solution(a):
    answer = 1
    left, right = 0, len(a)-1
    leftMinNumber, rightMinNumber = a[left], a[right]

    while left < right:
        if leftMinNumber < rightMinNumber:
            if a[right-1] < rightMinNumber:
                answer += 1
                rightMinNumber = a[right - 1]
            right -= 1
        else:
            if a[left + 1] < leftMinNumber:
                answer += 1
                leftMinNumber = a[left + 1]
            left += 1

    return answer

print(solution(a))