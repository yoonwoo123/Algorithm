import sys, itertools, time
start = time.time()
sys.stdin = open("야구_input.txt")
N = int(input())
arr = [list(map(int, list(input().split()))) for _ in range(N)]
# print(arr)
a = [_ for _ in range(1, 9)]
perm = list(itertools.permutations(a, 8))
# print(perm)
mymax = -1 # 가장큰값으로
for order in perm:
    order = list(order)
    order.insert(3, 0)
    # print(ening)
    cnt = -1
    tot = 0 # 총점
    for ening in arr:
        out = 0 # out 카운트
        batter = [0] * 3 # 4 이상이 되면 1점 추가하고 pop
        flag = 0
        while True:
            cnt += 1
            cnt %= 9
            if ening[order[cnt]] == 0:
                out += 1
                if out == 3:
                    break
                continue
            elif ening[order[cnt]] == 4:
                if flag:
                    tot += (sum(batter) + 1)
                    batter = [0] * 3
                    flag = 0
                else:
                    tot += 1
                continue
            # chk = 0
            if flag:
                for q in range(2, -1, -1):
                    if batter[q]:
                        if q + ening[order[cnt]] > 2:
                            tot += 1
                            batter[q] = 0
                        else:
                            batter[q + ening[order[cnt]]] = 1
                            batter[q] = 0
            batter[ening[order[cnt]] - 1] = 1
            flag = 1
    if mymax < tot:
        mymax = tot
print(mymax)
print(time.time()-start)