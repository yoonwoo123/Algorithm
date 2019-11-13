import sys, collections, copy, itertools
sys.stdin = open("잡페어2_input.txt")

tc = int(input())
for T in range(1, tc+1):
    bishops = input()
    print(bishops)

    table = [[0 for _ in range(8)] for q in range(8)]
