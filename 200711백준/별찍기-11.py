import sys, math
sys.stdin = open("별찍기_input.txt")

# 출처: https://has3ong.tistory.com/365
s = ['  *   ', ' * *  ', '***** ']

def make_stars(shift):
    for i in range(len(s)):
        s.append(s[i] + s[i])
        s[i] = ' '*shift+s[i]+' '*shift

N = int(input())
k = int(math.log(N/3, 2))

for i in range(k):
    make_stars(2**i*3)

print('\n'.join(s))