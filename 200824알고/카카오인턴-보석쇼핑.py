import copy
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    answer = []
    gemDict = {}
    for gem in gems:
        if gem not in gemDict:
            gemDict[gem] = 0

    left = len(gemDict)
    right = len(gems)

    while left <= right:
        mid = (left + right) // 2
        foundedGem = {}
        flag = False
        startPivot = 0
        endPivot = mid

        for i in range(startPivot, endPivot):
            if gems[i] not in foundedGem:
                foundedGem[gems[i]] = 1
            else:
                foundedGem[gems[i]] += 1

        endPivot -= 1
        if len(foundedGem) == len(gemDict):
            answer.append([mid, startPivot + 1, endPivot + 1])
            flag = True

        for i in range(len(gems) - mid):
            foundedGem[gems[startPivot]] -= 1
            if foundedGem[gems[startPivot]] == 0:
                foundedGem.pop(gems[startPivot])
            startPivot += 1
            endPivot += 1

            if gems[endPivot] not in foundedGem:
                foundedGem[gems[endPivot]] = 1
            else:
                foundedGem[gems[endPivot]] += 1

            if len(foundedGem) == len(gemDict):
                answer.append([mid, startPivot + 1, endPivot + 1])
                flag = True

        if flag:
            right = mid - 1
        else:
            left = mid + 1

    answer.sort()
    answer[0].pop(0)
    return answer[0]

print(solution(gems))