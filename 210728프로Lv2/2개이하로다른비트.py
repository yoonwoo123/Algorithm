numbers = [2, 7]

# bin() 을 통해서 십진수 -> 이진수로
# xor 연산 ^ 을 통해서 1의 개수가 1~2개인지 체크
def solution(numbers):
    answer = []

    for number in numbers:
        binary = str(bin(number))
        oneCnt = 0

        for i in range(len(binary) - 1, 1, -1):
            if binary[i] == '0': break
            oneCnt += 1

        oneCnt = max(oneCnt, 1)
        answer.append(number + 2 ** (oneCnt - 1))

    return answer

print(solution(numbers))