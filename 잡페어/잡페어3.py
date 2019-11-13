import sys, collections, copy, itertools
sys.stdin = open("잡페어3_input.txt")

tc = int(input())
for T in range(1, tc+1):
    sticker = list(map(int, input().split()))
    # print(sticker)
    sticker.append(0)
    sticker.append(0)
    slen = len(sticker)
    answer = -1

    i = 0
    tot = 0
    while True:
        # for x in range(1, 2):
        if slen-1 <= i: break
        mval = max(sticker[i], sticker[i+1], sticker[i+2])
        tot += mval
        for x in range(i, i+3):
            if mval == sticker[x]:
                i = x + 2
                break
    print(tot)
    answer = tot