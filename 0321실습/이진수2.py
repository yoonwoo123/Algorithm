import sys
sys.stdin = open('이진수2_input.txt')

tc = int(input())
for T in range(1, tc+1):
    N = float(input())
    total = []
    flag = 0
    for i in range(1, 14):
        total.append(int((N // 2**(-i))))
        N = N % 2**(-i)
        if N == 0:
            flag = 1
            break
    if len(total) > 12 and flag == 0:
        print("#%d overflow" % T)
    else:
        print("#%d %s" % (T, ''.join(map(str, total))))