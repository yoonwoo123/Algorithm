import sys
sys.stdin = open('이진수_input.txt')

asc = [[0, 0, 0, 0], # 0
       [0, 0, 0, 1], # 1
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]] # F

def aToh(c):
    if c <= '9':return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

tc = int(input())
for T in range(1, tc+1):
    N, sixteen = input().split()
    N = int(N)

    t = []

    # print(arr)
    for i in range(N):
        makeT(aToh(sixteen[i]))
    print('#%d %s' % (T, "".join(map(str, t))))