import sys, collections
sys.stdin = open("frog_input.txt")

X, Y, D = map(int, input().split())

if X == Y:
    print(0)
res = (Y - X) // D
if (Y - X) % D != 0:
    res += 1
print(res)