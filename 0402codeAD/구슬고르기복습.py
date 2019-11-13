import sys
sys.stdin = open("구슬고르기_input.txt")

# 김은경 샘 코드
def DFS1(n): # 중복순열
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        arr[n]=i
        DFS1(n+1)

def DFS3(n): # 순열
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        if chk[i]:continue
        chk[i]=1 # 순열은 체크 해야함
        arr[n]=i
        DFS3(n+1)
        chk[i]=0 # 순열은 체크해제도 해야함

def DFS2(n, start): # 중복조합
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7): # 시작은 스타트부터
        arr[n]=i
        DFS2(n+1, i) # 스타트업데이트는 start가 아닌 i

def DFS4(n, start): # 조합
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 5):
        arr[n]=i
        DFS4(n+1, i+1) # 조합은 i 가 아닌 i + 1 중요!


#main---------------------------------
N, M = map(int, input().split())
arr =[0] * (N+1)
chk = [0] * 7
if M ==1: DFS1(1)
elif M ==3 : DFS3(1)
elif M == 2: DFS2(1, 1)
elif M ==4: DFS4(1, 1)

# def ovperm(n, k):
#     if n == k:
#         for g in p:
#             print(g, end=" ")
#         print()
#     else:
#         for i in range(k, n):
#             a[i], a[k] = a[k], a[i]
#             p[k] = a[i]
#             perm(n, k+1)
#             # perm(n-1, k+1)
#             a[i], a[k] = a[k], a[i]
#
# def DFS(no): # chk를 하면 순열 chk를 하지 않으면 중복순열
#     if no >= N:
#         for i in range(N):
#             print(b[i], end=" ")
#         print()
#         return
#     for i in range(6):
#         # if chk[i]:continue # 1이면 continue, 0이면 진행
#         # chk[i] = 1
#         b[no] = a[i]
#         DFS(no + 1)
#         # chk[i] = 0
#
# def comb(no):
#     if no >= N:
#         for i in range(N):
#             print(b[i], end=" ")
#         print()
#         return
#     b[no] = a[no]
#     comb(no + 1)
#     b[no] = 0
#     comb(no + 1)
#
# # def combs(no, start): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
# #     for i in range(N): print(b[i], end=" ")
# #     print()
# #     if no >= N or start >= N:
# #         return
# #     for i in range(start, N):
# #         b[no] = a[i]
# #         combs(no+1, i+1)
# #         b[no] = 0
#
# N = int(input())
# a = [n for n in range(1, 7)]
# b = [0] * N
# chk = [0] * N
# # DFS(0)
# # comb(0)
# DFS(0)

def ovperm(no):
    if no >= N:
        print(a)
    return

    # else:
    for i in range(N):
        a[no] = i
        ovperm(no + 1)

def perm(no):
    if no >= N:
        print(a)
    return

    for i in range(N):
        if chk[i] == 1: continue
        chk[i] = 1
        a[no] = i
        perm(no + 1)
        chk[i] = 0

def ovcomb(no, start):
    if no >= N:
        print(a)
    return
    for i in range(start, N):
        a[no] = i
        ovcomb(no + 1, i)


def ovcomb(no, start):
    if no >= N:
        print(a)
    return
    for i in range(start, N):
        a[no] = i
        ovcomb(no + 1, i + 1)

