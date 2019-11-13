def paper(n) :
    if n == 1:
        return 1
    if n  % 2 == 0:
        return paper(n-1) * 2 + 1
    else:
        return paper(n-1) * 2 - 1

import sys
sys.stdin = open("0214_종이붙이기_input.txt")
testcases = int(input())
for T in range(testcases):
    N =int(input())
    print(f'#{T+1} {paper(N//10)}')