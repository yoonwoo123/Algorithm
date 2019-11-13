import sys
sys.stdin = open("input.txt")


def DFS1(n): # 중복순열
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        arr[n]=i # 빈 배열
        DFS1(n+1)

def DFS3(n): # 순열 중복을 제거하려면 체크했다 안했다!
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(1, 7):
        if chk[i]:continue
        chk[i]=1 # 체크했다
        arr[n]=i
        DFS3(n+1)
        chk[i]=0 # 체크안했다

def DFS2(n, start): # 중복조합 조합은 start도 가져간다
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7):
        arr[n]=i
        DFS2(n+1, i)

def DFS4(n, start): # 조합
    if n>N:
        for i in range(1, N+1): print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7):
        arr[n]=i
        DFS4(n+1, i+1) # 중복조합에서 +1만 다른것


#main---------------------------------
N, M = map(int, input().split())
arr =[0] * (N+1)
chk = [0] * 7
if M ==1: DFS1(1)
elif M ==3 : DFS3(1)
elif M == 2: DFS2(1, 1)
elif M ==4: DFS4(1,1)
