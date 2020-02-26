import sys, re
sys.stdin = open("다트게임_input.txt")

dartResult = input()

# answer = 0
# scores = []
# tmp = '' # 숫자가 되기 전 모아두는 곳
# for char in dartResult:
#     if char == 'S':
#         scores.append(int(tmp))
#         tmp = ''
#     elif char == 'D':
#         scores.append(int(tmp)**2)
#         tmp = ''
#     elif char == 'T':
#         scores.append(int(tmp)**3)
#         tmp = ''
#     elif char == '*':
#         if len(scores) == 1:
#             scores[-1] *= 2
#         else:
#             scores[-1] *= 2
#             scores[-2] *= 2
#     elif char == '#':
#         scores[-1] *= -1
#     else: # 숫자
#         tmp += char
# answer = sum(scores)

bonus = {'S' : 1, 'D' : 2, 'T' : 3}
option = {'' : 1, '*' : 2, '#' : -1}
p = re.compile('(\d+)([SDT])([*#]?)')
dart = p.findall(dartResult)
print(dart)
for i in range(len(dart)):
    if dart[i][2] == '*' and i > 0:
        dart[i-1] *= 2
    dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
print(dart)
answer = sum(dart)
print(answer)