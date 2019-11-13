import sys
sys.stdin = open("주사위던지기2_input.txt")

def DFS(no, nsum):
    global N
    if no > N:
        if nsum == M:
            for i in range(1, N+1):
                print(arr[i], end=" ")
            print()
        return
    for i in range(1, 7): # 1 ~ 6 깢의 눈
        arr[no] = i
        DFS(no+1, nsum + i)

# 눈의 중복을 배제한 순열
def DFS2(no, nsum):
    global N
    if no > N:
        if nsum == M:
            for i in range(1, N + 1):
                print(arr[i], end=" ")
            print()
        return
    for i in range(1, 7):  # 1 ~ 6 까지의 눈
        if chk[i] == 1:
            continue
        chk[i] = 1 # 사용한 눈 체크
        arr[no] = i # 눈 기록
        DFS2(no + 1, nsum + 1)
        chk[i] = 0 #눈 체크 해제

N, M = map(int, input().split())
arr = [0] * 8 # 주사위별 눈 기록
chk = [0] * 7
DFS(1, 0) # 1번 주사위부터 시작