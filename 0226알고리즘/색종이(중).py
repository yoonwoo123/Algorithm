import sys
sys.stdin = open("색종이(중)_input.txt")

N = int(input())
table = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0 ]

diax = [-1, 1]
diay = [-1, 1]
diax2 = [-1, 1]
diay2 = [1, -1]

for i in range(N):
    zero = 0
    cnt = 0
    w, h = map(int, input().split())
    for _ in range(110): # 도화지
        table.append([0] * 110)
    for x in range(w, w+10):
        for y in range(h, h+10):
            table[x][y] = 1
    for x in range(100):
        for y in range(100):
            if table[x][y] == 1:

                dia = 0
                dia2 = 0
                if x+1 > 110 or y+1 >110 or x - 1 < 0 or y - 1 <0:
                    continue
                for t in range(4):
                    if table[x + dx[t]][y + dy[t]] == 0:
                        zero += 1

print(zero)