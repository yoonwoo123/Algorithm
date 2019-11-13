import sys, collections
sys.stdin = open("점심식사_input.txt")

# tc = int(input())
# for T in range(1, tc+1):
#     N = int(input())
#     table = []
#     stairs = []
#
#     for x in range(N):
#         table.append(list(map(int, input().split())))
#         for y in range(N):
#             if table[x][y] > 1:
#                stairs.append([x, y, table[x][y]])
def dfx(dep):
    if dep == n:
        div(A)
        return
    else:
        for i in range(2):
            A[dep] = i
            dfx(dep + 1)
            A[dep] = 0

def div(H):
    s1 = []
    s2 = []
    for i in range(n):
        if H[i] == 1:
            s1.append(p[i])
        else:
            s2.append(p[i])
    solve(s1, s2)


def solve(s1, s2):
    global ans
    wait = [[], []]
    down = [[], []]
    info = [[], []]
    for i in s1:
        d = abs(i[1] - stare[0][0]) + abs(i[2] - stare[0][1])
        info[0].append(d)
    for i in s2:
        d = abs(i[1] - stare[1][0]) + abs(i[2] - stare[1][1])
        info[1].append(d)
    info[0].sort()
    info[1].sort()
    T = 1
    flag = 0
    while True:
        for num in range(2):
            if down[num]:
                for i in range(len(down[num])):
                    down[num][i] -= 1
                for _ in range(len(down[num])):
                    if down[num][0] == 0:
                        down[num].pop(0)

            if wait[num]:
                for _ in range(len(wait[num])):
                    if len(down[num]) < 3:
                        wait[num].pop(0)
                        down[num].append(stare[num][2])

            if info[num]:
                for _ in range(len(info[num])):
                    if info[num][0] == T:
                        wait[num].append(info[num].pop(0))
                    # else:
                    #     info[num].append(info[num].pop(0))

        if info == [[], []] and wait == [[], []] and down == [[], []]:
            break
        T += 1
    ans = min(ans, T)


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 9999
    stare = []
    p = []
    # 계단,사람 좌표를 저장
    pn = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:
                stare.append([i, j, arr[i][j]])
            elif arr[i][j] == 1:
                p.append([pn, i, j])
                pn += 1

    total = 0
    n = len(p)
    A = [0] * n

    dfx(0)
    print('#{} {}'.format(tc + 1, ans))