import sys
sys.stdin = open("항구배_input.txt")

tc = int(input())
for T in range(1, tc+1):
    happy = []
    N = int(input())
    for i in range(N):
        happy.append(int(input()))
