import sys
sys.stdin = open('그룹나누기_input.txt')

def find(x):
    if x == p[x]: return x
    else: return find(p[x])

tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())

    p = list(range(N+1)) # makeset
    arr = list(map(int, input().split()))

    for i in range(M):
        p1 = find(arr[i*2])
        p2 = find(arr[i*2 + 1])
        p[p2] = p1
    for i in range(1, N+1):
        p[i] = find(p[i])
    print('#%d %d' % (T, len(set(p))-1))