import sys
sys.stdin = open('암호_input.txt')

tc = int(input())
pwd = [[0,0,0,1,1,0,1], # 0
       [0,0,1,1,0,0,1], # 1
       [0,0,1,0,0,1,1],
       [0,1,1,1,1,0,1],
       [0,1,0,0,0,1,1],
       [0,1,1,0,0,0,1],
       [0,1,0,1,1,1,1],
       [0,1,1,1,0,1,1],
       [0,1,1,0,1,1,1],
       [0,0,0,1,0,1,1]] # 9

# 뒤에서부터 찾자 0이면 넘어가고 1일때부터 암호이다. insert(0)으로 앞으로쌓자

for T in range(1, tc+1):
    serial = []
    line = []
    flag = 0
    N, M = map(int, input().split())
    for _ in range(N):
        line.append(list(map(int, input()))) # 일단 인풋다받자

    for z in range(N):
        if sum(line[z]) == 0:
            continue
        line[z] = line[z][::-1]
        for i in range(M):
            if line[z][i] == 1:
                while True:
                    tmp = []
                    for j in range(7):
                        tmp.insert(0, line[z][i+j])
                    for x in range(10):
                        if tmp == pwd[x]:
                            serial.insert(0, x)
                    i += 7
                    if i > M-6:
                        flag = 1
                        break
                    elif len(serial) == 8:
                        flag = 1
                        break
                break
        if flag == 1:
            break
    # print(serial)
    odd_sum = 0
    even_sum = 0
    for i in range(1, 9):
        if i % 2 == 1:
            odd_sum += serial[i-1]
        else:
            even_sum += serial[i-1]
    if (odd_sum * 3 + even_sum) % 10 == 0:
        print('#%s %d' % (T, sum(serial)))
    else:
        print('#%s %d' % (T, 0))