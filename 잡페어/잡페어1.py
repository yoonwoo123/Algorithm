import sys, collections, copy, itertools
sys.stdin = open("잡페어1_input.txt")

tc = int(input())
for T in range(1, tc+1):
    goods = list(map(int, input().split()))
    boxes = list(map(int, input().split()))

    goods.sort()
    boxes.sort()
    # print(goods)
    # print(boxes)
    glen = len(goods)
    tot = 0
    for box in boxes:
        if box >= goods[tot]:
            tot += 1
            if tot == glen:
                break
    answer = tot
    print(answer)