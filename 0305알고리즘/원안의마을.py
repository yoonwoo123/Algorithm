import sys, math
sys.stdin = open("원안의마을_input.txt")

table = []
rs = []
N = int(input())
for i in range(N):
    table.append(list(map(int, list(input()))))

for x in range(N):
    for y in range(N):
        if table[x][y] == 2:
            x2 = x
            y2 = y
            break
for x1 in range(N):
    for y1 in range(N):
        if table[x1][y1] == 1:
            rs.append(math.ceil(((x2-x1)**2 + (y2-y1)**2)**0.5))
print(max(rs))