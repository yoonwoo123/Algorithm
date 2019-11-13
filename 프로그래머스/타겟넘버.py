import sys
sys.stdin = open("타겟넘버_input.txt")

numbers = list(map(int, input().split()))
target = int(input())

def DFS(dep):
    global answer
    if dep == N:
        # print(chk)
        tot = 0
        for i in range(N):
            if chk[i] == 0: # +
                tot += numbers[i]
            else:
                tot -= numbers[i]
        if tot == target:
            answer += 1
        return

    for i in range(2):
        chk[dep] = i
        DFS(dep + 1)
        chk[dep] = 0

N = len(numbers)
chk = [0] * N
answer = 0

DFS(0)
print(answer)