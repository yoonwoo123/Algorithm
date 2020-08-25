import itertools
expression = "100-200*300-500+20"

def solution(expression):
    def calculator(A, B, oper):
        if oper == '+': return A + B
        if oper == '-': return A - B
        if oper == '*': return A * B

    answer = 0
    tmp = ''
    expArr = []
    operation = ['+', '-', '*']
    for i in range(len(expression)):
        if expression[i] in operation:
            expArr.append(int(tmp))
            expArr.append(expression[i])
            tmp = ''
        else:
            tmp += expression[i]
    expArr.append(int(tmp))

    origin = expArr[:]
    for perm in itertools.permutations(operation, 3):
        for oper in perm:
            deleteIndex = []
            for i in range(len(expArr)):
                if expArr[i] == oper:
                    expArr[i+1] = calculator(expArr[i-1], expArr[i+1], oper)
                    deleteIndex.append(i-1)
                    deleteIndex.append(i)
            for i in range(len(deleteIndex) - 1, -1, -1):
                index = deleteIndex[i]
                expArr.pop(index)
        answer = max(answer, abs(expArr[0]))
        expArr = origin[:]
    return answer

print(solution(expression))