import sys
sys.stdin = open("새로운연산_input.txt")

tc = int(input())
for T in range(1, tc+1): # y가 행 x가 열
    P, Q = map(int, input().split())
    x = 1
    y = 1
    p_y = 1
    num = 1
    total_x = 0
    total_y = 0
    flag = 0

    while True:
        if num == P:
            total_x += x
            total_y += y
            flag += 1
        if num == Q:
            total_x += x
            total_y += y
            flag += 1
        elif flag == 2 and total_x == x and total_y == y:
            print('#%d %d' % (T, num))
            break
        if y == 1:
            p_y += 1
            y = p_y
            x = 1
            num += 1
        elif y != 1:
            x += 1
            y -= 1
            num += 1