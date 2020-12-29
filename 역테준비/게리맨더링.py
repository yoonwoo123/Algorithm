import sys, collections
sys.stdin = open("게리맨더링_input.txt")
input = sys.stdin.readline

N = int(input())
table = [[0 for _ in range(N+1)] for _ in range(N+1)]

peoples = list(map(int, input().split()))
for i in range(1, N+1):
    line = list(map(int, input().split()))

    for j in range(1, len(line)):
        num = line[j]
        table[i][num] = table[num][i] = 1


# for l in table:
#     print(l)
# print()