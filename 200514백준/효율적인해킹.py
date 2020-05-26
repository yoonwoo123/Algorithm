import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("효율적인해킹_input.txt")
input = sys.stdin.readline

def BFS(com, trust):
    q = [com]
    visited = [0 for i in range(N+1)]
    count = 0
    while q:
        current = q.pop()
        if not visited[current]:
            count += 1
            visited[current] = 1
            q += trust[current]
    return count

N, M = map(int, input().split())
trust = [[] for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

table = [0 for _ in range(N+1)]
for k in range(1, N+1):
    if trust[k]:
        table[k] = BFS(k, trust)

my_max = max(table)
print(*sorted([i for i in range(len(table)) if table[i] == my_max]))


# def DFS(com, visited):
#     global tot
#
#     if not visited[com]:
#         visited[com] = 1
#         tot += 1
#         for next in trust[com]:
#             DFS(next, visited)
#     return tot
#
# N, M = map(int, input().split())
# ans = [0 for _ in range(N+1)] # com번호와 갯수로 갯수가 최대인 것을 구하는 것
# trust = [[] for i in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     trust[B].append(A)
#
# for i in range(1, N+1):
#     tot = 1
#     ans[i] = DFS(i, [0 for _ in range(N+1)])
# my_max = max(ans)
# print(*sorted([i for i in range(len(ans)) if ans[i] == my_max]))
