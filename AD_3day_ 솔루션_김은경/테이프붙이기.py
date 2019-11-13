import sys
sys.stdin = open("input.txt")
def DFS(no, hap, cnt):
    global tot, nmin
    if cnt + (N-no)<N//2: return # 남은 잔량을 더해도 N/2 개가 안되면 리턴
    if cnt == N // 2:  # N/2개를 고르면 차의 최소를 구함
        temp = abs(hap - (tot - hap))
        nmin = min(nmin, temp)
        return
    if no>=N: return
    rec[cnt]=arr[no]
    DFS(no+1, hap+arr[no], cnt+1) # 테이프 붙이기
    rec[cnt]=0
    DFS(no+1, hap, cnt) # 붙이지 않기기
# main --------------------------
N = int(input())
arr = list(map(int, input().split()))
rec = [0]*N
tot = sum(arr)
nmin = 500*10
DFS(0, 0, 0)
print(nmin)
