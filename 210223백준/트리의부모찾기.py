import sys, collections
sys.stdin = open("트리의부모찾기_input.txt")
input = sys.stdin.readline

# 출처: https://suri78.tistory.com/136
N = int(input())
head = [0 for _ in range(N + 1)]
head[1] = 1
tree = {}

for i in range(1, N+1):
    tree[i] = []

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

q = collections.deque([1])
while q:
    node = q.popleft()
    for child in tree[node]:
        if not head[child]:
            head[child] = node
            q.append(child)

for h in head[2:]:
    print(h)