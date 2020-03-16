import sys
sys.stdin = open("기타줄_input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
minp, mino = 9999, 9999
for _ in range(M):
    p, o = map(int, input().split())
    minp = min(minp, p)
    mino = min(mino, o)
if minp >= mino * 6:
    print(mino*N)
else:
    r = N % 6
    if r * mino > minp:
        print(minp * (N // 6 + 1))
    else:
        print(minp * (N // 6) + mino * r)
