import sys
sys.stdin = open("공항_input.txt")

def parent_find(x):
    if x == parent[x]: # 부모노드가 자기 자신이다 -> 말단노드 즉 가장뿌리이다.
        return x
    p = parent_find(parent[x]) # 부모가 자기자신이 아니라면 찾을때까지 재귀
    # 즉 최종적으로 나오는 p 값은 가장뿌리값이 나올것
    parent[x] = p # x의 최상위 부모는 p로 설정
    return p

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y # x의 부모를 y로 즉 x의 부모를 x-1로

G = int(input())
P = int(input())
planes = []
for _ in range(P):
    planes.append(int(input()))

res = 0
parent = {i:i for i in range(G+1)}
# print(parent)
cnt = 0
for plane in planes:
    x = parent_find(plane)
    if x == 0: # 최상위 부모가 0이면 더 이상 비행기 도킹 x
        break
    union(x, x-1)
    cnt += 1
print(cnt)