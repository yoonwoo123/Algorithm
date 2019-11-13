def search(obj):
    s = []
    for char in obj:
        if char == '(' or char == '{':
            s.append(char)
        if char == ')' or char == '}':
            if len(s) == 0:
                return 0
            else:
                a = s.pop()
                if char != a:
                    continue
    if len(s) != 0:
        return 0
    else:
        return 1

import sys
sys.stdin = open('0214_괄호검사_input.txt')

testcases = int(input())
for T in range(testcases):
    # cash = list(map(int,(input().split())))
    chars = input()
    print(f'#{T+1} {search(chars)}')
