s = "3people unFollowed me"

def solution(s):
    answer = ''
    flag = 1
    for char in s:
        if char == ' ':
            flag = 1
            answer += char
        else:
            if flag:
                flag = 0
                answer += char.upper()
            else:
                answer += char.lower()

    return answer

print(solution(s))