import sys, collections
sys.stdin = open("rotate_input.txt")

A = list(map(int, input().split()))
K = int(input())

L = len(A)
if L == 0:
    print([])
else:
    cnt = K % L

if cnt == 0:
    print(A)
else:
    print(A[(L-cnt):] + A[:(L-cnt)])