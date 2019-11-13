import sys, copy, time, collections
sys.stdin = open("무선충전_input.txt")


dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
tc = int(input())
for T in range(1, tc+1):
    M, A = map(int, input().split()) # 이동 시간, 충전기 개수
    Amove = list(map(int, input().split()))
    Bmove = list(map(int, input().split()))
    BCs = []
    for _ in range(A):
        x, y, C, P = map(int, input().split())
        BCs.append([y-1, x-1, C, P])
    tot = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(A):
        x, y, c, p = BCs[i][0], BCs[i][1], BCs[i][2], BCs[i][3]
        if x + y <= c:
            if tmp1 < p:
                tmp1 = p
        if abs(x - 9) + abs(y - 9) <= c:
            if tmp2 < p:
                tmp2 = p
    tot += tmp1 + tmp2

    Ax, Ay = 0, 0
    Bx, By = 9, 9
    for i in range(M):
        nAx, nAy = Ax + dx[Amove[i]], Ay + dy[Amove[i]]
        nBx, nBy = Bx + dx[Bmove[i]], By + dy[Bmove[i]]
        Apowers = [0] * A
        Bpowers = [0] * A
        cnt = [0, 0]
        for i in range(A):
            x, y, c, p = BCs[i][0], BCs[i][1], BCs[i][2], BCs[i][3]
            if abs(x - nAx) + abs(y - nAy) <= c:
                Apowers[i] = p
                cnt[0] += 1
            if abs(x - nBx) + abs(y - nBy) <= c:
                Bpowers[i] = p
                cnt[1] += 1
        if min(cnt) == 0:
            tot += max(Apowers) + max(Bpowers)
        else:
            mymax = 0
            for a in range(A):
                for b in range(A):
                    if b == a:
                        if Apowers[a] == Bpowers[b]:
                            if mymax < (Apowers[a] + Bpowers[b]) // 2:
                                mymax = (Apowers[a] + Bpowers[b]) // 2
                    else:
                        if mymax < Apowers[a] + Bpowers[b]:
                            mymax = Apowers[a] + Bpowers[b]
            tot += mymax

        Ax, Ay = nAx, nAy
        Bx, By = nBx, nBy
    print(f'#{T} {tot}')