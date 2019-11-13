import sys
sys.stdin = open("게리맨더링2_input.txt")

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

