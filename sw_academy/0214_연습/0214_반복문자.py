# def duple(string):
#     l = len(string)
#     for i in range(l - 1):
#         if split[i] == split[i + 1]:
#             split[i] = '0'
#             split[i+1] = '0'
#     strs = ''.join(split)
#     result = strs.replace('0','')
#     if l == 1:
#         return result
#     return duple(result)
import sys
sys.stdin = open('0214_반복문자_input.txt')

testcases = int(input())
for T in range(testcases):
    char = input().split()[0]
    v = []
    for i in range(len(char)):
        if len(v) == 0:
            v.append(char[i])
            continue
        if v[-1] != char[i]:
            v.append(char[i])
            continue
        if v[-1] == char[i]:
            v.pop()
    print(f'#{T+1} {len(v)}')

