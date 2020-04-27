import itertools
n = 50
weak = [1, 5, 10, 12, 22, 25, 29, 30, 33, 36, 39, 42, 44, 46, 49]
dist = [4, 3, 2, 1, 5, 7, 6, 8]

def solution(n, weak, dist):
    answer = 999999
    s = 1
    perms = list(itertools.permutations(dist, len(dist)))
    c = 0
    for i in range(len(weak)):
        for perm in perms:
            c += 1
            ridx = lidx = i
            table = [0] * n
            rev_table = [0] * n
            for q in range(len(weak)):
                table[weak[q]] = 1
                rev_table[weak[q]] = 1

            repair = 0  # 시행횟수 , n 번 고치면 종료
            rev_repair = 0
            cnt = 0 # 몇명이 들어갔는지 구하고자 하는값
            r_cnt = 0
            # print(perm)
            flag1 = 1
            flag2 = 1
            for person in perm:
                cnt += 1
                if flag1:
                    while True:
                        ridx %= len(weak)
                        if table[weak[ridx]]:
                            start = weak[ridx]
                            break
                        else:
                            ridx += 1
                    # print(start, person)
                    for x in range(start, start+person+1):
                        x %= n # index 에러 방지
                        if table[x]:
                            repair += 1
                            table[x] = 0

                    if repair >= len(weak):
                        answer = min(answer, cnt)
                        flag1 = 0

                if flag2:
                    r_cnt += 1
                    while True:
                        lidx %= len(weak)
                        if rev_table[weak[lidx]]:
                            rev_start = weak[lidx]
                            break
                        else:
                            lidx += 1
                    for x in range(person+1):
                        idx = rev_start - x
                        if idx < 0:
                            idx = -(-idx % n)

                        if rev_table[idx]:
                            rev_repair += 1
                            rev_table[idx] = 0
                    if rev_repair >= len(weak):
                        answer = min(answer, r_cnt)
                        flag2 = 0
    print(c)
    if answer == 999999:
        return -1
    else:
        return answer

print(solution(n, weak, dist))
