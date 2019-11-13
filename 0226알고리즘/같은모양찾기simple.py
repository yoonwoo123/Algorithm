import sys
sys.stdin = open('같은모양찾기simple_input.txt')

table = []
pattern = []
M = int(input())

for i in range(M):
    table.append(list(map(int, list(input()))))

P = int(input())
for i in range(P):
    pattern.append(list(map(int, list(input()))))
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
print(res)