import sys, math
sys.stdin = open("회전초밥(중)_input.txt")
# 1 for , while, 배열 2개
# line = []
# res = 0
#
# N, d, k, c = map(int, input().split())
# for i in range(N):
#     line.append(int(input()))
# line += line
# i = 0
# while i < N:
#     eat = []
#     for x in range(i, i+k):
#         if line[x] == c:
#             i = x+1
#             break
#         if line[x] not in eat: # 가짓수 중복은 제외
#             eat.append(line[x])
#         i += 1
#     if c not in eat:
#         eat.append(c)
#     if res < len(eat):
#         res = len(eat)
# print(res)

# 2 for와 배열 1개 set 1개
line = []
res = 0
N, d, k, c = map(int, input().split())
for i in range(N):
    line.append(int(input()))
# line += line
for i in range(N):
    eat = set()
    eat.add(c)
    for x in range(i, i+k):
        if x >= N:
            x %= N
        eat.add(line[x])
    if res < len(eat):
        res = len(eat)
print(res)

# 3 for 와 배열 2개
# line = []
# res = 0
# N, d, k, c = map(int, input().split())
# for i in range(N):
#     line.append(int(input()))
# for i in range(N):
#     eat = []
#     for x in range(i, i+k):
#         if x >= N:
#             x %= N
#         if line[x] not in eat:
#             eat.append(line[x])
#     if c not in eat:
#         eat.append(c)
#     if res < len(eat):
#         res = len(eat)
# print(res)