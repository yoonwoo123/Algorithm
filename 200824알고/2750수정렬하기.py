import sys
sys.stdin = open("수정렬하기_input.txt")
I = sys.stdin.readline
O = sys.stdout.write

N = int(I())
A = []

for _ in range(N):
    A.append(int(I()))
A.sort()

O('\n'.join(map(str, A)))