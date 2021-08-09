a = [-5, 0, 2, 1, 2]
edges = [[0,1],[3,4],[2,3],[0,3]]

# 우선 a의 sum이 0이 아니라면 -1 반환 (0이여야만 가중치를 전부 0으로 만들 수 있다.)
# 트리구조이기 때문에 트리의 말단노드로 가서 시작해야 최소 횟수로 가중치를 0으로 만들 수 있다.
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    global answer
    def DFS(prev, current):
        global answer

        visited[current] = 1
        for node in tree[current]:
            if visited[node]: continue
            DFS(current, node)

        if prev == -1: return

        answer += abs(a[current])
        a[prev] += a[current]
        a[current] = 0

    answer = 0
    tree = {}

    if sum(a) != 0: return -1

    for x, y in edges:
        if x not in tree:
            tree[x] = [y]
        else:
            tree[x].append(y)

        if y not in tree:
            tree[y] = [x]
        else:
            tree[y].append(x)

    visited = [0 for _ in range(len(a))]
    DFS(-1, 0)

    if a[0] != 0:
        return -1

    return answer

print(solution(a, edges))