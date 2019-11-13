import sys
sys.stdin = open("input.txt")
def check(r, c): # 세로, 양대각선 체크 함수
    dc = [-1, 0,  1]
    dr = [-1, -1, -1]
    for i in range(3): # 3방향
        for k in range(1, N): # 1배, 2배 ...떨어진 거리
            nr = r + dr[i] * k
            nc = c + dc[i] * k
            if nr<0 or nr>=N or nc<0 or nc>=N : break #범위 벗어나면 탈출
            if arr[nr][nc]==1 : return 0 # 퀸이 놓였으면 실패
    return 1 # 성공
def DFS(no): # 현재행(no)에서 모든 열에 퀸을 놓아보는 경우의 수
    global sol
    if no>=N:
        sol+=1
        return
    for i in range(N): #  열
        if chk1[i] : continue # 세로방향체크
        if chk2[no + i]: continue # 우방향대각선체크
        if chk3[(N-1)-(no-i)]: continue # 좌방향대각선 체크
        chk1[i] = chk2[no + i] =  chk3[(N-1)-(no-i)] =1 # 퀸놓기
        DFS(no+1)
        chk1[i] = chk2[no + i] =  chk3[(N-1)-(no-i)] = 0  # 퀸빼기
        # if check(no, i): # 현좌표에 퀸을 놓을수 있다면
        #arr[no][i]=1 # 퀸놓기
        #DFS(no+1) # 다음행으로
        #arr[no][i] = 0 #퀸빼기

#main------------------------------------
N = int(input())
arr = [[0]*N for _ in range(N)]
chk1 =[0]*N
chk2 = [0]*N*2
chk3 = [0]*N*2
sol =0
DFS(0)
print(sol)

