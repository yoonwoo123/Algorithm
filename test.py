# import sys
# sys.stdin = open("0124_workshop_input.txt")
# testcases = input()
#
# for T in range(int(testcases)):
#
#
#     def replay(m): # input 넣어줘야함
#         no = int(input())  # 금속막대 개수
#         data = list(map(int, input().split()))
#         male = []
#         female = []
#         first = 0
#         m = 0
#         for i in range(no * 2):
#             if i % 2 == 0:
#                 male.append(data[i])
#
#         for i in range(no * 2):
#             if i % 2 == 1:
#                 female.append(data[i])
#
#         for i in range(no * 2):
#             # if i % 2 == 0 and data[i] not in female:
#             if data[i] in male and data[i] not in female:
#                 # print(male[i//2], end=" ") # 처음 들어가는 숫나사 번호
#                 first = i
#         m = first // 2 + 1
#         # replay(m)
#         for i in range(len(male)):
#             if m == male[i]:
#                 print(male[i], end=" ")
#                 print(female[i], end=" ")
#                 m = female[i]
#                 replay(m)
# replay(0)
a = [[1,2],[2,3]]
print(a[0])