N = 21232323

def solution(N):
    def validateNumber(num):
        nextNumber = ""
        isDuplicate = 0

        for digit in str(num):
            if len(nextNumber) == 0:
                nextNumber += digit
                continue

            if isDuplicate:
                nextNumber += "0"
                continue

            if digit == nextNumber[-1]:
                nextNumber = str(int(nextNumber + digit) + 1)
                isDuplicate = 1

            else:
                nextNumber += digit

        if isDuplicate:
            return validateNumber(int(nextNumber))

        return int(nextNumber)

    answer = validateNumber(N + 1)

    return answer

print(solution(N))
