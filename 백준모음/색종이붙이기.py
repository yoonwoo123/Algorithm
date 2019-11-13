import sys, collections
sys.stdin = open("색종이_input.txt")

def DFS(s): # 0, 0, 0
    global res

    if res < sum(chk): return # 가지치기

    if max(chk) > 5: # 5개 이상해서 쓸수 없음
        return
    if s >= O:
        if res > sum(chk):
            res = sum(chk)
            # print(chk)
        return

    x, y = ones[s][0], ones[s][1]
    if table[x][y]:
        for i in range(5, 0, -1):
            # print(chk)
            # for g in table:
            #     print(g)
            # print()
            if x + i >= 11 or y + i >= 11: continue
            if check(x, y, i): continue # 못지우는거면 컨티뉴


            for r in range(x, x + i):
                for c in range(y, y + i):
                    table[r][c] = 0 # 0으로바꿈
            chk[i] += 1  # chk함수
            DFS(s + 1)
            chk[i] -= 1
            for r in range(x, x + i):
                for c in range(y, y + i):
                    table[r][c] = 1 # 1으로 원래값
    else:
        DFS(s + 1)

def check(x, y, i):
    for r in range(x, x + i):
        for c in range(y, y + i):
            if table[r][c] == 0: return 1
    return 0

ones = []
table = []
res = 9999
for i in range(10):
    table.append(list(map(int, input().split())))
    for j in range(10):
        if table[i][j]:
            ones.append([i, j])
O = len(ones)
chk = [0] * 6
DFS(0)
if res == 9999:
    print(-1)
else:
    print(res)