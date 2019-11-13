import sys, collections
sys.stdin = open("전자카트_input.txt")

def perm(n, k, tot):
    global res
    if res <= tot: return
    if n == k:
        tot += arr[0][a[0]] # 회사에서 첫번째 고객
        for i in range(N-2):
            tot += arr[a[i]][a[i+1]]
            if res <= tot: return
        tot += arr[a[-1]][0] # 마지막 - 회사
        if res > tot:
            res = tot
    else:
        for i in range(k, n): # k = depth, n = 찾고자 하는 갯수
            a[i], a[k] = a[k], a[i]
            perm(n, k+1, tot) # depth =  k+1
            a[i], a[k] = a[k], a[i] # 원래 값으로 복귀

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    arr = []
    res = 99999999999999
    for i in range(N):
        arr.append(list(map(int, input().split())))
    a = [x for x in range(1, N)]
    # print(a)
    perm(N-1, 0, 0)
    print('#%d %d' % (T, res))
