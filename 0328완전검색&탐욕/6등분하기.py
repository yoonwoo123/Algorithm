import sys
sys.stdin = open("6등분하기_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split()))) # 판 생성

    res = []
    for x in range(1, N):
        for y in range(1, M-1):
            for z in range(y+1, M):
                six = []

                p1 = 0
                p2 = 0
                p3 = 0
                p4 = 0
                p5 = 0
                p6 = 0
                # 더해줘야함
                for i in range(x):
                    for j in range(y):
                        p1 += arr[i][j]
                    for j in range(y, z):
                        p2 += arr[i][j]
                    for j in range(z, M):
                        p3 += arr[i][j]
                six.append(p1)
                six.append(p2)
                six.append(p3)

                for i in range(x, N):
                    for j in range(y):
                        p4 += arr[i][j]
                    for j in range(y, z):
                        p5 += arr[i][j]
                    for j in range(z, M):
                        p6 += arr[i][j]
                six.append(p4)
                six.append(p5)
                six.append(p6)
                six.sort()
                tot = 0
                tot += abs(six[-1] - six[0])
                tot += abs(six[-1] - six[1])
                tot += abs(six[0] - six[1])
                res.append(tot)
    print('#%d %d' % (T, max(res)))