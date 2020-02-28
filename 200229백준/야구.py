import sys, itertools
sys.stdin = open("야구_input.txt")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, list(input().split()))) for _ in range(N)]
mymax = 0 # 가장큰값으로
for order in itertools.permutations(range(1, 9), 8):
    order = list(order[:3]) + [0] + list(order[3:])
    hitter = 0
    tot = 0 # 총점
    for inning in arr:
        out = 0 # out 카운트
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            htype = inning[order[hitter]]
            if htype == 0:
                out += 1
            elif htype == 1:
                tot += b3
                b1, b2, b3 = 1, b1, b2
            elif htype == 2:
                tot += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif htype == 3:
                tot += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                tot += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            hitter = (hitter + 1) % 9
    mymax = max(mymax, tot)
print(mymax)