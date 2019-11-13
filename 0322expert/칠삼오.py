import sys
sys.stdin = open('칠삼오_input.txt')


def myprint(q):
    while q != 0:
        q = q - 1
        total.append(T[q])
        # print(" %d " % (T[q]), end = "")
def comb(n, r, q):
    if r == 0:
        myprint(q)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

tc = int(input())
for TC in range(1, tc+1):
    total = []
    res = set()
    A = list(map(int, input().split()))

    # A = [1, 2, 3, 4]
    T = [0] * 3
    comb(7, 3, 3)
    for i in range(len(total)// 3):
        res.add(total[3*i] + total[3*i+1] + total[3*i+2])
    print('#{} {}'.format(TC, sorted(res)[::-1][4]))