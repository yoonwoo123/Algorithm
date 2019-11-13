import sys
sys.stdin = open("input.txt")
def DFS(no, nsum):
    global nmin
    if nsum>nmin: return
    if no>=N:
        for i in range(N): print(rec[i], end=' ')
        print(nsum)
        if nsum<nmin: nmin = nsum
        return
    for i in range(N):
        if chk[i] : continue # 사용한 장소이면 스킵
        chk[i]=1 # 장소 체크
        rec[no]=arr[no][i] # 기록
        DFS(no+1 , nsum+arr[no][i])
        chk[i]=0 # 장소 체크 해제
#main-------------------------
N = int(input())
rec = [0]*N # 기록 배열
chk = [0]*N #  장소 사용여부 체크배열
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
nmin=0x7fffffff
DFS(0, 0) # 0 행부터 시작, 합계는 0
print(nmin)