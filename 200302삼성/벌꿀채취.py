import sys, itertools
sys.stdin = open("벌꿀채취_input.txt")
input = sys.stdin.readline

tc = int(input())
for T in range(1, tc+1):
    N, M, C = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            A = [0] * M
            acomb = ()
            amax = 0
            for m in range(M, 0, -1):
                for comb in itertools.combinations(range(j, j+M), m):
                    totA = 0
                    for idx in comb:
                        totA += table[i][idx]
                    if amax <= totA <= C:
                        amax = totA
                        acomb = comb
            apos = []
            c = 0
            for n in acomb:
                A[c] = table[i][n]
                table[i][n] = 0
                apos.append((i, n, A[c]))
                c += 1
            for x in range(i, N):
                for y in range(N-M+1):
                    if table[x][y]:
                        B = [0] * M
                        acomb = ()
                        amax = 0
                        flag = 0
                        for m in range(M, 0, -1):
                            if flag: break
                            for comb in itertools.combinations(range(y, y + M), m):
                                totA = 0
                                for idx in comb:
                                    if table[x][idx] == 0:
                                        flag = 1
                                        break
                                    totA += table[x][idx]
                                if flag: break
                                if amax <= totA <= C:
                                    amax = totA
                                    acomb = comb
                        c = 0
                        bpos = []
                        for n in acomb:
                            B[c] = table[x][n]
                            table[x][n] = 0
                            bpos.append((x, n, B[c]))
                            c += 1
                        tot = 0
                        for num in A:
                            tot += num*num
                        for num in B:
                            tot += num*num
                        ans = max(ans, tot)
                        for xpos, ypos, v in bpos:
                            table[xpos][ypos] = v
                for xpos, ypos, v in apos:
                    table[xpos][ypos] = v
    print(f'#{T} {ans}')