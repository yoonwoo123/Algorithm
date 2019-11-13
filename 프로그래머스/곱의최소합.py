import sys
sys.stdin = open("곱의최소합_input.txt")

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A.sort()
B.sort(reverse=True)

L = len(A)
for i in range(L):
    answer += A[i] * B[i]
print(answer)