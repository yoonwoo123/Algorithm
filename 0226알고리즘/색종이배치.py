import sys
sys.stdin = open("색종이배치_input.txt")

# 1 : 꼭짓점이 맞닿은것(1개만) 2 : 라인이 맞닿은것(한줄) 3: 면이 겹치는것(여러줄) 4: 하나도 겹치지않는것

x_1, y_1, w_1, h_1 = map(int, input().split())
x_2, y_2, w_2, h_2 = map(int, input().split())

table = []
for _ in range(100):
    tmp = [0] * 100
    table.append(tmp)
# print(table)
for x in range(h_1+1): # 색종이 1 생성
    for y in range(w_1+1):
        table[x + x_1][y + y_1] += 1

for x in range(h_2+1): # 색종이 2 생성
    for y in range(w_2+1):
        table[x + x_2][y + y_2] += 1
cnt = 0
for x in range(100): # 테이블을 돌면서 2가 몇개있는지 확인
    for y in range(100):
        if table[x][y] == 2:
            cnt += 1


if cnt == 1:
    print(1)
if cnt == 0:
    print(4)
if cnt > 1:
    if x_1+w_1 == x_2 or x_2 +w_2 == x_1 or y_1 + h_1 == y_2 or y_2 + h_2 == y_1:
        print(2)

    else:
        print(3)

