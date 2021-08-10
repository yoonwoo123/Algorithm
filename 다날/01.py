arr = [1, 1, 3, 3, 0, 1, 1]

def solution(arr):
    answer = []
    meetNumber = -1

    for num in arr:
        if num != meetNumber:
            answer.append(num)
            meetNumber = num

    return answer

print(solution(arr))