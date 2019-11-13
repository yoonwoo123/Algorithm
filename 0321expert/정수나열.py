import sys
sys.stdin = open("정수나열_input.txt")

# tc = int(input())
# for T in range(1, tc+1):
#     N = int(input())
#     if N > 20:
#         numbers = []
#         if N % 20 == 0:
#             cases = int(N // 20)
#         else:
#             cases = int(N // 20 + 1)
#         for _ in range(cases):
#             tmp = list(input().split())
#             for num in tmp:
#                 numbers.append(num)
#     else:
#         numbers = list(input().split())
#
#     flag = 0
#     for i in range(10):
#         if str(i) not in numbers: # 한자릿수
#             print('#%d %d' % (T, i))
#             flag = 1
#             break
#
#     if flag == 0:
#         dou = []
#         for x in range(N - 1):
#             dou.append(int(numbers[x] + numbers[x + 1]))
#         dou = dou[::-1]
#         for i in range(10, 100):
#             if i in dou:
#                 continue
#             elif i not in dou:
#                 print('#%d %d' % (T, i))
#                 flag = 1
#                 break
#     if flag == 0:
#         tri = []
#         for x in range(N - 2):
#             tri.append(int(numbers[x] + numbers[x + 1] + numbers[x + 2]))
#         tri = tri[::-1]
#         # print(tri)
#         for i in range(100, 1001):
#             if i in tri:
#                 continue
#             elif i not in tri:
#                 print('#%d %d' % (T, i))
#                 break
test = int(input())

for tc in range(1, test + 1):
    N = int(input())
    num = []
    result = 0
    while len(num) != N:
        num.extend(input().split())

    num = ''.join(num)

    while str(result) in num:
        result += 1

    print('#{} {}'.format(tc, result))