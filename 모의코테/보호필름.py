import sys, itertools, copy
sys.stdin = open("보호필름_input.txt")

def DFS(dep):
    global res, table
    if res < K: return
    if res <= sum(chk):return

    if dep == D:
        film = []
        for x in range(D):
            if chk[x] == 1:  # 체크된 행에 약품을 뿌리자
                film.append(x)  # flim에 약을 뿌려야할 리스트를 모아둔다.
        flen = len(film)

        if flen:
            A = [0, 1]  # 2개로 중복순열
            perm = list(itertools.product(A, repeat=flen))
            for nums in perm:
                tmp = []
                for x in range(flen):
                    for y in range(W):
                        table[film[x]][y] = nums[x]

                if check():
                    tot = sum(chk)
                    if res > tot:
                        res = tot
                    # print(chk)
                    # for g in table:
                    #     print(g)
                    # print()
                    for x in range(flen):
                        for y in range(W):
                            table[film[x]][y] = ori[film[x]][y]
                    return

            for x in range(flen):
                for y in range(W):
                    table[film[x]][y] = ori[film[x]][y]

        else:
            if check():
                tot = sum(chk)
                if res > tot:
                    res = tot
        return

    for i in range(2):
        chk[dep] = i  # 체크가 1이면 어펜드하는 부분집합
        DFS(dep + 1)
        chk[dep] = 0
        if res < K: return


def check():
    c = 0
    flag = 0
    for y in range(W):
        ab = [0, 0]  # A 카운트 B 카운트
        for x in range(D):
            if table[x][y] == 0:
                ab[0] += 1
                ab[1] = 0
            else:
                ab[1] += 1
                ab[0] = 0
            if max(ab) >= K:
                c += 1
                flag = 1
                break
        if flag == 0: break

    if c == W:
        return 1 # 전부 통과
    return 0


tc = int(input())
for T in range(1, tc + 1):
    D, W, K = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(D)]
    chk = [0] * D
    res = 999999999
    ori = copy.deepcopy(table)

    DFS(0)
    print(f'#{T} {res}')