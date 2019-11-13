import sys
sys.stdin = open("DFSBFS_input.txt")

def DFS(V):
    global cnt
    print(V, end=" ")
    cnt += 1
    if cnt >= N: return
    for i in range(N+1):
        if cnt >= N: break
        if arr[V][i] == 1 and chk[i] == 0:
            # print(i)
            chk[i] = 1 # 방문체크
            DFS(i)

def BFS(V):
    global cnt
    q = []
    q.append(V)
    chk[V] = 1
    print(V, end=" ")
    while q:
        if cnt >= N-1: break
        V = q.pop(0)
        for i in range(N+1):
            if arr[V][i] == 1 and chk[i] == 0:
                print(i, end=" ")
                q.append(i)
                chk[i] = 1
                cnt += 1
                if cnt >= (N-1):
                    break

N, M, V = map(int, input().split())
tmp = []
for i in range(M):
    tmp.append(list(map(int, input().split())))

arr = [[0 for _ in range(N+1)] for r in range(N+1)]
chk = [0] * (N + 1) # chk 함수 방문체크용
cnt = 0
for i in range(M): # 쌍방향으로 찾아줘야함
    arr[tmp[i][0]][tmp[i][1]] = 1
    arr[tmp[i][1]][tmp[i][0]] = 1
#
# for g in arr:
#     print(g)
# print()
#
# print(tmp)

chk[V] = 1
DFS(V)
print()
chk = [0] * (N + 1)
cnt = 0
BFS(V)