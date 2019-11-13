import sys
sys.stdin = open("N-Queen_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N = int(input)
    table = [[0 for _ in range(N)] for _ in range(N)]
    # BT 이용해서 가지치기도 활용할수있음해보자