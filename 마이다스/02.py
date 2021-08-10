n = 4
v1 = [1, 3]
v2 = [2, 4]
num = [2, 2]
amount = [1, -2]

def solution(n, v1, v2, num, amount):
    def findParent(x):
        if parent[x] == x:
            return x

        return findParent(parent[x])

    def makeLeader():
        for i in range(len(v1)):
            parentV1 = findParent(v1[i])
            parentV2 = findParent(v2[i])

            if parentV1 < parentV2:
                parent[parentV2] = parentV1
            else:
                parent[parentV1] = parentV2

    def makeTeam():
        for i in range(1, len(parent)):
            team[findParent(parent[i])] = 0

    def calculateScore():
        for i in range(len(num)):
            teamLeader = findParent(num[i])
            team[teamLeader] += amount[i]

    def findLeaderOfMaxScore():
        leaderOfMaxScoreTeam = 0
        maxScore = -9999999

        for leader, score in team.items():
            if score > maxScore:
                maxScore = score
                leaderOfMaxScoreTeam = leader

            elif score == maxScore:
                leaderOfMaxScoreTeam = min(leaderOfMaxScoreTeam, leader)

        return leaderOfMaxScoreTeam

    parent = [x for x in range(n + 1)]
    team = {}

    makeLeader()
    makeTeam()
    calculateScore()
    answer = findLeaderOfMaxScore()

    return answer

print(solution(n, v1, v2, num, amount))