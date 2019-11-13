import sys, itertools
sys.stdin = open("그래프칠하기_input.txt")

def check(no, color):
    # 현 노드와 연결된 인접한 노드와 중복 색상 여부 체크
    for i in range(no):
        if arr[no][i] and rec[i] == color:
            return False
    return True

def DFS(no):
    global sol
    # if sol : return
    if no >= N:
        sol = 1
        return
    # 현재 노드에게 1~M번색까지 모두 칠해보는 경우의 수
    # 현노드에게 현 색상을 칠할 수 있으면 칠하고 다음 노드로 진행
    for i in range(1, M+1): # 1~M 색상
        if check(no, i): # 현노드에게 현 색상을 칠할 수 있으면
            rec[no] = i # 색상 기록
            DFS(no+1)
            if sol: return
        # for j in range(i):
        #     if arr[i][j] == 1:
        #         rec[i] = color
        # rec[i] =


N, M = map(int, input().split())
arr = []
sol = 0
rec = [0] * N # 노드별 색상기록배열
for i in range(N):
    arr.append(list(map(int, input().split())))

sol = 0
DFS(0) # 0 번 노드부터 시작
if sol:
    for i in range(N):
        print(rec[i], end=" ")
else: print(-1)