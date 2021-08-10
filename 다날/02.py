s = "baabaa"

def solution(s):
    meetChar = [s[0]]

    for i in range(1, len(s)):
        if len(meetChar) == 0 or s[i] != meetChar[-1]:
            meetChar.append(s[i])
        else:
            meetChar.pop()

    if len(meetChar) == 0:
        answer = 1
    else:
        answer = 0

    return answer

print(solution(s))