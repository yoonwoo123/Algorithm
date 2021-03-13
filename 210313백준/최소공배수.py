import sys
sys.stdin = open("최대공배수_input.txt")

def gcd(A, B):
    while B:
        A, B = B, A % B

    return A

tc = int(input())
for T in range(1, tc + 1):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))