import sys
sys.stdin = open('빙고_input.txt')

table = []
bingo_num = []
for i in range(5): # 빙고판 생성
    tmp = list(map(int ,input().split()))
    table.append(tmp)

for i in range(5): # 빙고숫자배열 생성
    numbers = list(map(int ,input().split()))
    for num in numbers:
        bingo_num.append(num)
cnt = 0
for x in range(5):
    for y in range(5):
        if table[x][y] == bingo_num[cnt]:
            table[x][y] = 0 # 맞는 빙고를 0으로 지우기

            cnt += 1   # 횟수 1 증가

# for i in range(len(bingo_num)):
#     if bingo_num[i]
print(bingo_num)

# 나중에 사회자가 부른 수 = bingo_num의 인덱스 + 1