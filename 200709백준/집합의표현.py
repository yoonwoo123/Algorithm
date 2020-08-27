import sys
sys.stdin = open("집합의표현_input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

# 유니온 파인드로 합집합을 만들땐 뿌리부모를 같은걸로 해주고
# 같은 집합에 포함되있나 검사는 부모가 같다면 yes 아니면 no

def parent_find(x):
    if parents[x] != x:
        parents[x] = parent_find(parents[x])
    return parents[x]

def union(a, b):
    a = parent_find(a)
    b = parent_find(b)
    parents[b] = a

parents = [x for x in range(N+1)]
for i in range(M):
    NO, A, B = map(int, input().split())
    if NO == 0:
        if A != B:
            union(A, B)
    else:
        if A == B:
            print('YES')
        else:
            if parent_find(A) == parent_find(B):
                # print를 조금 더 빠르게 해주는 것
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")
