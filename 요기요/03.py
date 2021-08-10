N = 994563213

def solution(N):
    def validateNumber(stringfiedNumber):
        nextNumber = ""
        isDuplicate = 0

        for digit in stringfiedNumber:
            if len(nextNumber) == 0:
                nextNumber += digit
                continue

            if isDuplicate:
                nextNumber += "0"
                continue

            if digit == nextNumber[-1]:
                if digit != "9":
                    nextNumber += str(int(digit) + 1)
                else:
                    nextNumber = str(int(nextNumber + digit) + 1)

                isDuplicate = 1

            else:
                nextNumber += digit

        if isDuplicate:
            return validateNumber(nextNumber)

        return int(nextNumber)

    answer = validateNumber(str(N + 1))

    return answer

print(solution(N))