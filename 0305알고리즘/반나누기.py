import sys
sys.stdin = open("반나누기_input.txt")

T = int(input())
for i in range(T):
    score = []
    res = []

    N, K_min, K_max = map(int, input().split())
    scores = list(map(int, input().split()))

    for x in scores:
        if x not in score:
            score.append(x)
    sortscore = sorted(score)[::-1]

    for y in range(len(sortscore)-1):
        T2 = sortscore[y]
        for d in range(1, len(sortscore)):
            T1 = sortscore[d]
            sclass = [0] * 3
            for q in scores:
                if q >= T2:
                    sclass[0] += 1
                elif T1 <= q < T2:
                    sclass[1] += 1
                elif q < T1:
                    sclass[2] += 1
            if min(sclass) >= K_min and max(sclass) <= K_max and min(sclass) != 0:
                res.append(max(sclass) - min(sclass))
    if len(res) == 0:
        print(-1)
    else:
        print(min(res))