import sys
sys.stdin = open('연습1_input.txt')
#
# for _ in range(7):
#     numbers = list(map(int, list(input())))
# res = ""
# for _ in range(10):
#     total = 0
#     for i in range(7):
#         if numbers[i] == 1:
#             total = 2**(6-i)
#     res += str(total)
# print(res)

arr = list(map(int, input()))

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + arr[j]
    print(n, end=" ")
print()