import sys
sys.stdin = open('최소합_input.txt')

dx = [0, 1] # 우, 하
dy = [1, 0]

def DFS(x, y, tot):
    if len(res) > 0 and res[-1] <= tot:
        return
    flag = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            flag += 1
            continue
        DFS(nx, ny, tot + arr[nx][ny])
    if flag == 2:
        res.append(tot)

tc = int(input())
for T in range(1, tc+1):
    N = int(input())
    res = []
    arr = []
    tot = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    DFS(0, 0, arr[0][0])
    print(res)
    print('#%d %d' % (T, min(res)))