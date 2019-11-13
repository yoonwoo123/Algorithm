import sys, collections

def BFS():
    q = collections.deque()
    q.append([K, 0])
    dis = 100100 # 수의 차이
    while q:
        k, cnt = q.popleft() # 동생 위치

        if k % 2 == 0: # 짝수면 2로 나눠주자.
            nk = k//2
            if abs(nk - N) < dis:
                dis = abs(nk - N)
                distant.append(dis)
                mincnt = cnt + 1
            else:
                res.append([abs(nk - N), cnt + 1])
                res.append([dis, mincnt])
                continue
            q.append([nk, cnt + 1])
            continue

        for i in range(2):
            nk = k + dx[i]
            q.append([nk, cnt + 1])

    return dis + mincnt

N, K = map(int, input().split())
dx = [1, -1]
res = []
distant = []

# print(BFS())
BFS()
# print(res)
# print(distant)

mymin = 99999
for a in res:
    if mymin > sum(a):
        mymin = sum(a)
print(mymin)