import sys, collections
sys.stdin = open("벽부수고이동_input.txt")
input = sys.stdin.readline

def BFS2(): # 벽 1개 부쉴때
    q = collections.deque()
    q.append((0, 0, 0))
    # q = [[0, 0, 0]]
    # bomb = 0
    while q:
        x, y, bomb = q.popleft()
        if x == N-1 and y == M-1:
            return memo[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if memo[nx][ny]:
                continue

            if arr[nx][ny] == '0':
                memo[nx][ny] = memo[x][y] + 1
                q.append((nx, ny, bomb))

            if arr[nx][ny] == '1' and bomb == 0:
                memo[nx][ny] = memo[x][y] + 1
                q.append((nx, ny, 1))
    return -1

N, M = map(int, input().split())
# 도착지점은 N-1, M-1  1,1 이 실은 0, 0 이기 때문
arr = [list(input()) for _ in range(N)]
memo = [[0 for x in range(M)] for y in range(N)]
memo[0][0] = 1 # 첫 시작 값
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# for i in range(N):
#     arr.append(list(map(int, list(input()))))

# for g in arr:
#     print(g)
# print()

print(BFS2())
# for g in arr:
#     print(g)
# print()

