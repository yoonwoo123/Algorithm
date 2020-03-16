import sys
input = sys.stdin.readline
N = list(input().rstrip())
N.sort(reverse=True)
if N[-1] != '0' or sum(map(int, N)) % 3 != 0:
    print(-1)
else:
    print(''.join(N))
