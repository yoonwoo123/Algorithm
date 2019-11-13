import sys
sys.stdin = open("보충학습과평균_input.txt")

tc = int(input())
for T in range(1, tc+1):
    total = 0
    scores = list(map(int, list(input().split())))
    for score in scores:
        if score >= 40:
            total += score
        else:
            total += 40
    print('#%d %d' % (T, int(total/5)))