import sys, itertools
sys.stdin = open("수진이의팰린드롬_input.txt")

# def FindTarget():
#     global tar
#     for num in range(LW + 1, 0, -1):  # 팰린드롬인지 탐색하는 문자길이
#         for perm in perms:
#             for i in range(LW-num+1):
#                 tmp = perm[i:i+num]
#                 rev = tmp[::-1]
#                 if tmp == rev:
#                     tar = perm
#                     return
#
# tc = int(input())
# for T in range(1, tc+1):
#     W = input()
#     LW = len(W)
#     arr = list(W)
#     perms = list(itertools.permutations(arr, LW))
#     # for perm in perms:
#     #     print(perm)
#     # print()
#     ans = 0
#     tar = ''
#     FindTarget()
#     # print(tar)
#     for num in range(LW + 1, 0, -1):  # 팰린드롬인지 탐색하는 문자길이
#         for i in range(LW - num + 1):
#             tmp = tar[i:i + num]
#             rev = tmp[::-1]
#             if tmp == rev:
#                 ans += 1
#     print(f'#{T} {ans}')

for t in range(int(input())):
    a = input()
    ans = 0
    word_dic = {}
    for x in a:
        if x in word_dic:
            word_dic[x] += 1
        else:
            word_dic[x] = 1
    for i in word_dic.values():
        ans += i * (i + 1) // 2

    print('#{} {}'.format(t + 1, ans))