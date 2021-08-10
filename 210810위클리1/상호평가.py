scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

def solution(scores):
    answer = ''
    grades = {"A": [90, 101], "B": [80, 90], "C": [70, 80], "D": [50, 70], "F": [0, 50]}

    for y in range(len(scores)):
        totalScore = 0
        scoreArr = []

        for x in range(len(scores)):
            totalScore += scores[x][y]
            scoreArr.append(scores[x][y])

        scoreArr.sort()
        if scoreArr[0] == scores[y][y] and scoreArr[0] != scoreArr[1]:
            totalScore -= scores[y][y]
            avgScore = totalScore // (len(scores) - 1)


        elif scoreArr[-1] == scores[y][y] and scoreArr[-1] != scoreArr[-2]:
            totalScore -= scores[y][y]
            avgScore = totalScore // (len(scores) - 1)

        else:
            avgScore = totalScore // len(scores)

        for grade, scoreRange in grades.items():
            if scoreRange[0] <= avgScore < scoreRange[1]:
                answer += grade
                break

    return answer

print(solution(scores))