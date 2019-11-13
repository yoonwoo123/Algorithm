import sys
sys.stdin = open("나는학급회장이다_input.txt")

N = int(input())
oth_cnt = [[0 for _ in range(4)] for _ in range(4)]

oth = [0] * 3
for i in range(N):
    scores = list(map(int, input().split()))
    for x in range(3):
        if x == 0:
            oth_cnt[1][scores[0]] += 1 # 점수
        elif x == 1:
            oth_cnt[2][scores[1]] += 1
        elif x == 2:
            oth_cnt[3][scores[2]] += 1
    oth[0] += scores[0]
    oth[1] += scores[1]
    oth[2] += scores[2]
idx = []
for i in range(3):
    if max(oth) == oth[i]:
        idx.append(i)


if oth.count(max(oth)) > 1:

    if oth_cnt[idx[1]][3] > oth_cnt[idx[2]][3] and oth_cnt[idx[1]][3] > oth_cnt[idx[3]][3]:
        print("%d %d" % (idx[0] + 1, max(oth)))
    elif oth_cnt[idx[2]][3] > oth_cnt[idx[1]][3] and oth_cnt[idx[2]][3] > oth_cnt[idx[3]][3]:
        print("%d %d" % (idx[1] + 1, max(oth)))
    elif oth_cnt[idx[3]][3] > oth_cnt[idx[1]][3] and oth_cnt[idx[3]][3] > oth_cnt[idx[2]][3]:
        print("%d %d" % (idx[2] + 1, max(oth)))

    else:
        if oth_cnt[idx[1]][2] > oth_cnt[idx[2]][2] and oth_cnt[idx[1]][2] > oth_cnt[idx[3]][2]:
            print("%d %d" % (idx[0] + 1, max(oth)))
        elif oth_cnt[idx[2]][2] > oth_cnt[idx[1]][2] and oth_cnt[idx[2]][2] > oth_cnt[idx[3]][2]:
            print("%d %d" % (idx[1] + 1, max(oth)))
        elif oth_cnt[idx[3]][2] > oth_cnt[idx[1]][2] and oth_cnt[idx[3]][2] > oth_cnt[idx[2]][2]:
            print("%d %d" % (idx[2] + 1, max(oth)))
        else:
            print("%d %d" % (0, max(oth)))


    # if oth_cnt[idx[1]][3] > oth_cnt[idx[2]][3]:
    #
    #     if oth_cnt[idx[1]][3] > oth_cnt[idx[3]][3]:
    #         print("%d %d" % (idx[0] +1, max(oth)))
    #     else:
    #         print("%d %d" % (idx[2] +1, max(oth)))
    #
    # elif oth_cnt[idx[1]][3] < oth_cnt[idx[2]][3]:
    #     if oth_cnt[idx[2]][3] < oth_cnt[idx[3]][3]:
    #         print("%d %d" % (idx[2] +1, max(oth)))
    #     else:
    #         print("%d %d" % (idx[1] +1, max(oth)))
    #
    # else:
    #     if oth_cnt[idx[1]][2] > oth_cnt[idx[2]][2]:
    #
    #         if oth_cnt[idx[3]][2] > oth_cnt[idx[1]][2]:
    #             print("%d %d" % (idx[2] + 1, max(oth)))
    #         else:
    #             print("%d %d" % (idx[0] + 1, max(oth)))
    #
    #     elif oth_cnt[idx[1]][2] < oth_cnt[idx[2]][2]:
    #         if oth_cnt[idx[2]][2] < oth_cnt[idx[3]][2]:
    #             print("%d %d" % (idx[2] + 1, max(oth)))
    #         else:
    #             print("%d %d" % (idx[1] + 1, max(oth)))
    #
    #     else:
    #         print("%d %d" % (0, max(oth)))

else:
    print("%d %d" % (idx[0]+1, max(oth)))
print(idx)
print(oth)
print(oth_cnt)