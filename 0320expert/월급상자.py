import sys
sys.stdin = open('월급상자_input.txt')

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    total = 0
    for _ in range(N):
        Pi, X = input().split()
        Pi = float(Pi)
        X = int(X)
        # print(Pi)
        total += Pi * X
    print('#%s %f' % (T, total))