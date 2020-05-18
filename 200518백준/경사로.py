import sys
sys.stdin = open("경사로_input.txt")

N, L = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x in range(N):
    current = table[x][0]
    cnt = 1 # 같은 높이의 땅이 몇개 있었나
    flag = True # flag가 False로 바뀌지 않는다면 ans += 1
    y = 1
    while y < N:
        if current == table[x][y]:
            cnt += 1
        elif table[x][y] - current == 1 and cnt >= L:
            cnt = 1
            current = table[x][y]

        elif current - table[x][y] == 1:
            if y + L - 1 >= N:
                flag = False
                break

            for i in range(1, L):
                if table[x][y+i] != table[x][y]:
                    flag = False
                    break
            if flag == False: break
            cnt = 0
            current = table[x][y]
            y = y + L - 1

        else:
            flag = False
            break
        y += 1
    if flag: ans += 1

for y in range(N):
    current = table[0][y]
    cnt = 1 # 같은 높이의 땅이 몇개 있었나
    flag = True # flag가 False로 바뀌지 않는다면 ans += 1
    x = 1
    while x < N:
        if current == table[x][y]:
            cnt += 1
        elif table[x][y] - current == 1 and cnt >= L:
            cnt = 1
            current = table[x][y]
        elif current - table[x][y] == 1:
            if x + L - 1 >= N:
                flag = False
                break

            for i in range(1, L):
                if table[x+i][y] != table[x][y]:
                    flag = False
                    break
            if flag == False: break
            cnt = 0
            current = table[x][y]
            x = x + L - 1
        else:
            flag = False
            break
        x += 1
    if flag: ans += 1

print(ans)