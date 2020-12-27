import sys
sys.stdin = open("행렬_input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
print(N, M)