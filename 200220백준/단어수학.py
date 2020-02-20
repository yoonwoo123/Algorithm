import sys, collections
sys.stdin = open("단어수학_input.txt")
input = sys.stdin.readline

N = int(input())
alphas = [0]*26
i = 0
while i < N:
    for j, c in enumerate(input().strip()[::-1]):
        alphas[ord(c)-ord('A')] += (10**j)
    i += 1
alphas.sort(reverse = True)
ans = 0
for i in range(10):
    ans += (alphas[i] * (9-i))
print(ans)