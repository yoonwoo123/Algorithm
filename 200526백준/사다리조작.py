import sys, itertools
sys.stdin = open("사다리조작_input.txt")

# 2를 만나면 왼쪽으로 가고 1을 만나면 오른쪽으로 가자
# i 세로줄 도달 i 값이 다르면 바로 break해서 효율을 높이자
def Go():
    for y in range(N):
        sy = y
        for x in range(H):
            if table[x][y] == 1:
                y += 1
            elif table[x][y] == 2:
                y -= 1
        if sy != y:
            return False
    return True

def solution():
    if Go():
        return 0

    poses = []  # 사다리를 넣을 수 있는 좌표후보들
    for x in range(H):
        for y in range(N - 1):
            if table[x][y] == 0 and table[x][y + 1] == 0:
                poses.append(((x, y), (x, y + 1)))

    for cnt in range(1, 4): # 1, 2, 3번까지
        for comb in itertools.combinations(poses, cnt):
            for posA, posB in comb:
                table[posA[0]][posA[1]] = 1
                table[posB[0]][posB[1]] = 2

            if Go():
                return cnt

            for posA, posB in comb:
                table[posA[0]][posA[1]] = 0
                table[posB[0]][posB[1]] = 0
    return -1

N, M, H = map(int, input().split())
table = [[0 for _ in range(N)] for q in range(H)]

for _ in range(M):
    x, y = map(int, input().split())
    table[x-1][y-1] = 1
    table[x - 1][y] = 2

print(solution())
