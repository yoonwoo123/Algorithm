import sys, collections
sys.stdin = open("월드컵_input.txt")

def sol():
    for team in table:
        if sum(team) != 5:
            return 0
    tots = [0, 0, 0]
    wins = []
    draws = []
    loses = []
    cnt = 0
    for y in (1, 3):
        for x in range(6):
            if y == 0 and table[x][y]:
                wins.append(table[x][y])
            elif y == 1 and table[x][y]:
                draws.append(table[x][y])
            elif y == 2 and table[x][y]:
                loses.append(table[x][y])
            tots[y] += table[x][y]
    if tots[0] != tots[2]: return 0

    while wins or loses:
        wins.sort(reverse=True)
        loses.sort(reverse=True)
        if wins[0] > len(loses) - 1: return 0
        cnt = 0
        for i in range(1, wins[0] + 1):
            loses[i] -= 1
            if loses[i] == 0:
                cnt += 1
        for i in range(cnt):
            loses.pop()
        wins.pop(0)


    while draws:
        draws.sort(reverse=True)
        if draws[0] > len(draws) - 1: return 0
        cnt = 0
        for i in range(1, draws[0] + 1):
            draws[i] -= 1
            if draws[i] == 0:
                cnt += 1
        for i in range(cnt):
            draws.pop()
        draws.pop(0)
    return 1

for T in range(4):
    scores = list(map(int, input().split()))
    table = []
    idx = 0
    for i in range(6): # 6팀의 승 무 패 를 2차원배열로
        table.append([scores[i*3], scores[i*3 + 1], scores[i*3 + 2]])
    # print(table)
    print(sol(), end=" ")