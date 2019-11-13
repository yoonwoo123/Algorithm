import sys
sys.stdin = open("미사일_input.txt")

def clear(i):
    for j in range(N):
        dist = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1]-arr[j][1])
        if dist<=R:
            arr[j][2]-=P

def update(i):
    for j in range(N):
        dist = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1]-arr[j][1])
        if dist<=R: arr[j][2]+=P

def DFS(no):
    global sol
    if no>M: # >= 아닌가요?
        cnt=0
        for i in range(N):
            if arr[i][2]>0: cnt+=1
        if cnt<sol: sol=cnt
        return

    for i in range(N):
        if arr[i][2]<=0 : continue # 미사일이 떨어진곳이 이미 침몰한 배면 에너지 감소하면 안됨
        clear(i)
        DFS(no+1)
        update(i)

#main -------------------------
N= int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
M, P, R = map(int, input().split())

sol=16
DFS(1)
print(sol)