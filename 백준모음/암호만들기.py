import sys
sys.stdin = open("암호_input.txt")

def DFS(cnt, s):
    # global tmp
    if cnt == L:
        b = 0
        j = 0
        for char in tmp:
            if char in bowl:
                b += 1
            else:
                j += 1
        if b > 0 and j > 1:
            print(''.join(tmp))
        return

    for i in range(s, C):
        tmp.append(arr[i])
        DFS(cnt + 1, i + 1)
        tmp.pop(-1)

bowl = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
tmp = []
DFS(0, 0)
# print(arr)