import sys
sys.stdin = open("네이버4_input.txt")

N = int(input())

seats = list(map(int, input().split()))
res = 0
si = -1

if sum(seats) == 1:
    for i in range(N):
        if seats[i] == 1:
            print(max(i, ((N-1) - i)))
            break
else:
    for i in range(N):
        if seats[i] == 1:
            if si == -1:
                si = i

            else:
                if res < i - si:
                    res = i - si
                si = i

    print(res//2)