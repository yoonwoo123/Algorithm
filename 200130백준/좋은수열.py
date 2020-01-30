import sys, heapq
sys.stdin = open("좋은수열_input.txt")

def DFS(L):
    for i in range(1, L // 2 + 1):  # L//2 번 만큼 반복
        if answer[L - i:L] == answer[L - 2 * i:L - i]: return

    if L == N:
        print(''.join(map(str, answer)))
        exit()

    for num in range(1, 4):
        answer.append(num)
        DFS(L + 1)
        answer.pop()

N = int(input())
answer = []
DFS(0)

