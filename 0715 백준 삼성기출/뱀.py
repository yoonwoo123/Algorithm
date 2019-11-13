import collections, sys

N = int(sys.stdin.readline())
table = [[0 for _ in range(N)] for r in range(N)]
table[0][0] = 1
K = int(sys.stdin.readline())

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    table[r-1][c-1] = 6 # 사과는 6으로 표현
    # 뱀은 1로 표현 0은 빈곳
# 뱀이 1행 1열에서 출발하는데 실제 idx는 0,0 이므로 1씩빼야함

L = int(sys.stdin.readline())
timelist = [0] * 10001
for _ in range(L):
    X, C = sys.stdin.readline().split()
    timelist[int(X)] = C

# for g in table:
#     print(g)
# print()

turn = [[2, 3], [3, 2], [1, 0], [0, 1]]
# L = 0 , D = 1
#     상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tot = 0 # 걸린 시간
tcnt = 3 # turn count 로 처음엔 오른쪽시작이니 3 시작

snake = collections.deque([[0,0]]) # 뱀의 머리 꼬리를 que로 표현 처음 뱀의 위치
    # for i in range(L):
def BFS():
    global tot, tcnt
    q = collections.deque([])
    q.append([0, 0])
    while q:
    # for t in range(1, 10001):
        nx = q[-1][0] + dx[tcnt]
        ny = q[-1][1] + dy[tcnt]
        tot += 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return tot
            # break # 벽에 부딪힘
        if table[nx][ny] == 1:
            return tot
            # break # 자기 몸과 부딪힘

        if table[nx][ny] != 6: # 사과를 만나지않았으면
            tx, ty = q.popleft() # 꼬리부분을 자른다.
            table[tx][ty] = 0 # 자른 꼬리부분을 비운다.

        q.append([nx, ny])  # 현재 머리위치 업데이트
        table[nx][ny] = 1  # 테이블에 표시
        # 만약 사과를 만났다면 꼬리도 남고 비우지도 않는다.

        if timelist[tot] == 'L':
            tcnt = turn[tcnt][0]
        elif timelist[tot] == 'D':
            tcnt = turn[tcnt][1]
BFS()
print(tot)