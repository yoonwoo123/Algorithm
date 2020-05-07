s = "abcdcba"

def solution(s):

    def check(left, right, cnt):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                cnt += 2
                left -= 1
                right += 1
            else:
                return cnt
        return cnt

    answer = 1
    for i in range(len(s)-1):
        flag = False
        if s[i] == s[i+1]:
            flag = True
            left = i - 1
            right = i + 2
            cnt1 = check(i - 1, i + 2, 2)

        cnt2 = check(i - 1, i + 1, 1)

        if flag:
            answer = max(answer, cnt1, cnt2)
        else:
            answer = max(answer, cnt2)

    return answer

print(solution(s))

# 문제가 개편 되었습니다. 이로 인해 함수 구성이 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(longest_palindrom("토마토맛토마토"))
# print(longest_palindrom("토마토맛있어"))