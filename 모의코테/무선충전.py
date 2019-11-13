import sys, copy, time, collections
sys.stdin = open("무선충전_input.txt")
# 모든 사용자의 충전량 합의 최대값

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
tc = int(input())
for T in range(1, tc + 1):
    M, A = map(int, input().split())  # 총 이동시간, 충전기개수
    uA = list(map(int, input().split()))
    uB = list(map(int, input().split()))
    uA.insert(0, 0)  # 0초때 체크하기위해 값 넣어줌
    uB.insert(0, 0)
    BCs = []
    scores = [[0 for y in range(M + 1)] for x in range(2)]  # 유저 두명 스코어보드

    for i in range(A):
        # X, Y, 충전범위C, 충전량P
        x, y, c, p = list(map(int, input().split()))
        BCs.append([y - 1, x - 1, c, p])
    # 시작점이 BC범위안이면 충전되야함
    # 움직일때마다 움직인 좌표값과 모든BC의 좌표값과 비교해서
    # 범위안에 드는 BC중 최대이익을 내는 곳을 선별해서 스코어보드반영
    # 한 범위안에 동시에 2명일 경우 이익을 고려해봐서 결정해야함
    # table을 만들어서 충전 범위안에 충전량을 써놓자.

    table = [[0 for _ in range(10)] for q in range(10)]
    for x in range(10):
        for y in range(10):
            for i in range(A):
                if abs(x - BCs[i][0]) + abs(y - BCs[i][1]) <= BCs[i][2]:
                    if table[x][y] != 0:  # 이미 다른 범위 안이라면?
                        if type(table[x][y]) == list:
                            table[x][y].append(BCs[i][3])
                            table[x][y].sort(reverse=True)
                        else:
                            ori = table[x][y]
                            if ori > BCs[i][3]:
                                table[x][y] = [ori, BCs[i][3]]
                            else:
                                table[x][y] = [BCs[i][3], ori]
                    else:
                        table[x][y] = BCs[i][3]
    for g in table:
        print(g)
    print()

    ax, ay = 0, 0
    bx, by = 9, 9
    for t in range(M + 1):  # 총 이동시간 돌린다.
        nax, nay = ax + dx[uA[t]], ay + dy[uA[t]]
        nbx, nby = bx + dx[uB[t]], by + dy[uB[t]]
        if type(table[nax][nay]) == list and type(table[nbx][nby]) == list:
            avals = table[nax][nay]  # list
            bvals = table[nbx][nby]  # list
            if avals[0] != bvals[0]:
                scores[0][t] += avals[0]
                scores[1][t] += bvals[0]
            else:
                for i in range(A): # 충전량이 같은 다른 BC인지 검증
                    if BCs[i][3] == avals[0]:
                        # 둘이 같은 BC이다.
                        if abs(nax - BCs[i][0]) + abs(nay - BCs[i][1]) <= BCs[i][2] and abs(nbx - BCs[i][0]) + abs(
                                nby - BCs[i][1]) <= BCs[i][2]:
                            if avals[1] >= bvals[1]:
                                scores[0][t] += avals[1]
                                scores[1][t] += bvals[0]
                            else:
                                scores[0][t] += avals[0]
                                scores[1][t] += bvals[1]
                            break
                        else:
                            scores[0][t] += avals[0]
                            scores[1][t] += bvals[0]
                            break
        elif type(table[nax][nay]) == list:
            avals = table[nax][nay]  # list
            bval = table[nbx][nby]

            if avals[0] != bval:
                scores[0][t] += avals[0]
                scores[1][t] += bval
            else:
                for i in range(A):
                    if BCs[i][3] == table[nbx][nby]:
                        # 둘이 같은 i
                        if abs(nax - BCs[i][0]) + abs(nay - BCs[i][1]) <= BCs[i][2] and abs(nbx - BCs[i][0]) + abs(
                                nby - BCs[i][1]) <= BCs[i][2]:
                            if avals[0] <= bval + avals[1]:
                                scores[1][t] += bval
                                scores[0][t] += avals[1]
                            else:
                                scores[1][t] += (avals[0] // 2)
                                scores[0][t] += (avals[0] // 2)
                            break
                        else:
                            scores[0][t] += avals[0]
                            scores[1][t] += bval
                            break

        elif type(table[nbx][nby]) == list:
            aval = table[nax][nay]
            bvals = table[nbx][nby]

            if aval != bvals[0]:
                scores[0][t] += aval
                scores[1][t] += bvals[0]
            else:
                for i in range(A):
                    if BCs[i][3] == table[nax][nay]:
                        # 둘이 같은 i
                        if abs(nax - BCs[i][0]) + abs(nay - BCs[i][1]) <= BCs[i][2] and abs(nbx - BCs[i][0]) + abs(
                                nby - BCs[i][1]) <= BCs[i][2]:
                            if bvals[0] <= aval + bvals[1]:
                                scores[1][t] += bvals[1]
                                scores[0][t] += aval
                            else:
                                scores[1][t] += (bvals[0] // 2)
                                scores[0][t] += (bvals[0] // 2)
                            break
                        else:
                            scores[0][t] += aval
                            scores[1][t] += bvals[0]
                            break
        else:
            if table[nax][nay] == table[nbx][nby]:
                for i in range(A):
                    if BCs[i][3] == table[nax][nay]:
                        # 둘이 같은 i
                        if abs(nax - BCs[i][0]) + abs(nay - BCs[i][1]) <= BCs[i][2] and abs(nbx - BCs[i][0]) + abs(
                                nby - BCs[i][1]) <= BCs[i][2]:
                            scores[0][t] += (table[nax][nay] // 2)
                            scores[1][t] += (table[nbx][nby] // 2)
                            break
                        else:
                            scores[0][t] += table[nax][nay]
                            scores[1][t] += table[nbx][nby]
                            break

            else:
                scores[0][t] += table[nax][nay]
                scores[1][t] += table[nbx][nby]
        ax, ay = nax, nay
        bx, by = nbx, nby

    for g in scores:
        print(g)

    tot = 0
    for i in range(2):
        tot += sum(scores[i])
    print(f'#{T} {tot}')
    # print('--')
