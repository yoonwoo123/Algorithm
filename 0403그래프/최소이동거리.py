import sys
sys.stdin = open('최소이동거리_input.txt')

# s: 시작 정점, A: 인접 행렬, D: 거리
# v: 정점 집합, U: 선택된 정점 집합 ( visited )

def Dijkstra(s, A, D):
    U = {s}

    for i in range(N):
        D[i] = A[s][i]

    while U

tc = int(input())
for T in range(1, tc+1):
    N, E = map(int, input(),split())
    A = [[0 for _ in range(E)] for _ in range(E)]
    D = [0] * E


    for i in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w
