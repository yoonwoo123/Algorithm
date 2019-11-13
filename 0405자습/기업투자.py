import sys
sys.stdin = open("기업투자_input.txt")
# 부분집합을 이용한 문제 N=4이면 1,2,3,4 중 합이 4가 되는 경우의 부분집합

def powerset(n, k):
    if n == k:
        tot = 0
        for i in range(N):
            if A[i] == 1:
                tot += data[i]
        if tot == 4:
            for i in range(N):
                if A[i] == 1:
                    print(data[i], end=" ")
            print()
        # print(tot)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

def perm(no):
    global my_max
    if no >= comp:
        # print(A)
        if sum(A) == N:
            # print(A)
            tot = 0
            for i in range(comp):
                tot += arr[A[i]][i]
            if my_max < tot:
                # print(A)
                my_max = tot
            # for i in range(comp):
            #     arr[A[i]]
        # for i in range(comp):
        #     print(A[i], end=" ")
        # print()
        return
    for i in range(N+1):
        A[no] = i
        perm(no + 1)

N, comp = map(int, input().split())
arr = [[0 for _ in range(comp)] for _ in range(N+1)]
A = [0] * comp
my_max = -1
for x in range(1, N+1):
    tmp = list(map(int, input().split()))
    for y in range(comp):
        arr[x][y] = tmp[y+1]
# print(arr)

perm(0)
print(my_max)