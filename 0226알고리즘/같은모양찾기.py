import sys
sys.stdin = open('같은모양찾기_input.txt')

table = []
pattern = []
pattern2 = []
M = int(input())

# def rot(cnt): # 회전 함수
#     for z in range(cnt):
#         for x in range(N):
#             for y in range(N):
#                 rotate[y][N - 1 - x] = table[x][y]

for i in range(M):
    table.append(list(map(int, list(input()))))

P = int(input())

for i in range(P): # 패턴 생성 패턴을 90, 180, 270 돌리면서 확인해서 총 패턴수를 구한다.
    pattern.append(list(map(int, list(input()))))

for i in range(P):
    pattern2.append([0]*P)

for x in range(P): # 90 도 돌아간 패턴2
    for y in range(P):
        pattern2[y][P - 1 - x] = pattern[x][y]

res = 0
for a in range(M-P+1):#  반복
        for b in range(M-P+1):
            cnt = 0
            for x in range(P):
                for y in range(P):
                    if pattern[x][y] == table[x + a][y + b]:
                        cnt += 1
            if cnt == P*P:
                res += 1

for a in range(M-P+1):#  90도
        for b in range(M-P+1):
            cnt = 0
            for x in range(P):
                for y in range(P):
                    if pattern2[x][y] == table[x + a][y + b]:
                        cnt += 1
            if cnt == P*P:
                res += 1

for x in range(P): # 180 도 돌아간 패턴1
    for y in range(P):
        pattern[y][P - 1 - x] = pattern2[x][y]

for a in range(M-P+1):#  180도에서 패턴찾기
        for b in range(M-P+1):
            cnt = 0
            for x in range(P):
                for y in range(P):
                    if pattern[x][y] == table[x + a][y + b]:
                        cnt += 1
            if cnt == P*P:
                res += 1

for x in range(P): # 270 도 돌아간 패턴2
    for y in range(P):
        pattern2[y][P - 1 - x] = pattern[x][y]

for a in range(M-P+1):#  270도 패턴찾기
        for b in range(M-P+1):
            cnt = 0
            for x in range(P):
                for y in range(P):
                    if pattern2[x][y] == table[x + a][y + b]:
                        cnt += 1
            if cnt == P*P:
                res += 1

print(res)
