import sys
sys.stdin = open("input.txt")

def DFS(no, nsum): # 현재 로봇(행)에서 모든 과자를 먹는 경우의수
    global nmin
    if nsum>nmin: return # 가지치기
    if no>=N:
        if nsum<nmin: nmin = nsum
        return
    for i in range(N): # 과자(열)
        if chk[i]: continue
        chk[i]=1
        DFS(no+1, nsum + arr[no][i])
        chk[i]=0

#main ------------------------------
T = int(input())
for ti in range(T):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))

    chk =[0]*N # 과자 체크배열
    arr =[[0]*N for _ in range(N)]
    for i in range(N): # 행을 로봇으로
        for j in range(N): # 열을 스택으로
            dist =  abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1] - snack[j*2+1])
            arr[i][j]= dist # 로봇별 과자와의 거리 기록
    # for i in range(N): # 행을 로봇으로
    #     print(arr[i])

    nmin = 0x7fffffff
    DFS(0, 0) # 0번 로봇부터 시작, 합계 0
    print(nmin)

