import sys, math
sys.stdin = open("최대공약수와최소공배수_input.txt")

# 최대공약수를 구하고 A * B // 최대공약수 = 최소공배수이다.

def myGcd(A, B):
    while B:
        A, B = B, A % B

    return A

A, B = map(int, input().split())
maxMeasure = myGcd(A, B)
print(maxMeasure)
print(A * B // maxMeasure) # 최소공배수