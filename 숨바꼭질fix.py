import sys, collections
sys.stdin = open("숨바꼭질_input.txt")

def BFS():
    while q:
        x = q.popleft()
        if x == K:
            return visit[x]
        nextPos(x - 1, x)
        nextPos(x + 1, x)
        nextPos(x * 2, x)

def nextPos(nex, x):
    # nex 지점이 범위 내에 있고
    # 한번도 방문하지 않았거나, 최소 time으로 해당 방을 방문한 경우
    if 0 <= nex < 100001 and (visit[nex] == 0 or visit[nex] > visit[x] + 1):
        visit[nex] = visit[x] + 1
        q.append(nex)



N, K = map(int, input().split())

visit = [0 for _ in range(100001)]
q = collections.deque([N])
print(BFS())