import sys, itertools
sys.stdin = open("N진수게임_input.txt")

n, t, m, p = map(int, input().split())

def nchange(num, n):
    q, r = divmod(num, n)
    NOT = NOTATION[r]
    return nchange(q, n) + NOT if q else NOT

answer = ''
NOTATION = '0123456789ABCDEF'
arr = ''
p -= 1
L = 0
for num in range(t*m):
    tmp = nchange(num, n)
    arr += tmp
    L += len(tmp)
    if L >= t*m: break
# for i in range(p, p + t * m, m):
#     answer += arr[i]
answer = arr[p::m][:t]
print(answer)