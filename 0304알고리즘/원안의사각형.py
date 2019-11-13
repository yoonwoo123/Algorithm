import sys
sys.stdin = open("원안의사각형_input.txt")

R = int(input())

root = 1.414
s = int((R * 0.414) //root)

total = 0

# 사분면을 4개로 나눠서 생각한다치고 사분면 1개 * 4 해주자

total = (R * R) - (s+1)**2

# 범위는 1부터 R - s
for i in range(1, R-s):
    total -= 2 * (int((((i**2 + R**2)**0.5 - R) // root)) + 1)
print(4*total)