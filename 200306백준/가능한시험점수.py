import sys
sys.stdin = open("가능한_input.txt")

tc = int(input())
for T in range(1, tc + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    Max = sum(arr)
    A = [0] * (Max + 1)
    A[0] = 1
    for i in arr:
        for j in range(Max - i, -1, -1):
            if A[j] == 1:
                A[j + i] = 1

    print(f'#{T} {sum(A)}')