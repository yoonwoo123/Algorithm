import sys
sys.stdin = open("input.txt")

def DFS(no, lastA, lastB, hap ):
    global sol
    if no>=N:
        if hap>sol: sol=hap
        return
    # A : 작은 상자순으로 포장하기
    if lastA>arr[no]: DFS(no+1, arr[no], lastB, hap+arr[no])
    # B : 큰 상자순으로 포장하기
    if lastB < arr[no]: DFS(no + 1, lastA, arr[no], hap + arr[no])
    # 현재 상자를 포장하기 않기
    DFS(no+1, lastA, lastB, hap)

# main ----------------------
T = int(input())
for ti in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sol=0
    DFS(0, 1000, 0, 0 ) # 0번상자부터 시작, A 초기값 1000, B  초기값 0, 합계 0
    print(sol)
