import sys, collections
sys.stdin = open("건물세우기_input.txt")
# 순열 사용
def perm(n, k, tot):
    global my_min
    # if my_min <= tot:
    #     return
    if n == k:
        print(a)
        print(tot)
        # tot = 0
        # for x in range(N):
        #     tot += arr[x][a[x]]
        if my_min > tot:
            my_min = tot
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1, tot + arr[i][a[i]])
            a[i], a[k] = a[k], a[i]

my_min = 99999999999999
arr = []
N = int(input())
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
a = [n for n in range(N)]
perm(N, 0, 0)
print(my_min)