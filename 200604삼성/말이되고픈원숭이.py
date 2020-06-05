import sys, itertools, collections
sys.stdin = open("말이되고픈원숭이_input.txt")

K = int(input())
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]
