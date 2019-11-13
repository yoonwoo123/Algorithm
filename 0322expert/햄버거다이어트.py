import sys
sys.stdin = open("햄버거다이어트_input.txt")

tc = int(input())
for T in range(1, tc+1):
    scokal = []
    N, L = map(int, input().split())
    for i in range(N):
        S, K = map(int, input().split())
        scokal.append([S, K])
    print(scokal)
