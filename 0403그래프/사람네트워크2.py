import sys
sys.stdin = open('사람네트워크_input.txt')

def floid():
    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != k and j != i:
                        arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])


tc = int(input())
for T in range(1, tc+1):
    tmp = list(map(int, input().split()))
    N = tmp.pop(0)
    arr = [[0 for _ in range(N)] for _ in range(len(tmp)//N)]
    for i in range(len(tmp)//N):
        for j in range(N):
            if i != j and tmp[j + N*i] == 0:
                arr[i][j] = 99999999999
                continue
            arr[i][j] = tmp[j + N*i]
    # for g in arr:
    #     print(g)
    # print()
    my_min = 9999999999999
    floid()
    for i in range(len(tmp)//N):
        if my_min > sum(arr[i]):
            my_min = sum(arr[i])
    print('#%d %d' % (T, my_min))
    # for g in arr:
    #     print(g)
    # print()