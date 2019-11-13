import sys
sys.stdin = open("nqueen_input.txt")
# 체크함수 3개를 만들자
# 우상 체크함수는 행과열을 더하면 체크인덱스가 나오고
# 좌상 체크함수는 공식을 찾아서 만든다 공식: (n-1) - (r-c)
def DFS(x): # 행
    global res
    if x >= N: # 행이 찾고자하는 N-1을 넘었을때 # 맞았는지 확인하려면 맨 위에서 체크하자
        res += 1
        return
    # for x in range(N):
    for y in range(N):
        if chk1[y] == 0 and chk2[x + y] == 0 and chk3[(N - 1) + (x - y)] == 0:
            # arr[x][y] = 1
            chk1[y] = chk2[x + y] = chk3[(N - 1) + (x - y)] = 1 # 방문체크
            DFS(x + 1) # 다음 행으로
            chk1[y] = chk2[x + y] = chk3[(N - 1) + (x - y)] = 0 # 방문체크해제

N = int(input())

chk1 = [0] * N # 세로열
chk2 = [0] * N *2 # 우상
chk3 = [0] * N *2 # 좌상
res = 0

DFS(0)
print(res)
