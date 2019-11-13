import sys
sys.stdin = open("베이비진_input.txt")



tc = int(input())
for T in range(1, tc+1):
    numbers = list(map(int, input().split()))
    p1 = []
    p2 = []
    flag = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(numbers[i])
            if len(p1) >= 3:
                p1.sort()
                for x in range(len(p1)):
                    if p1.count(x) >= 3:
                        flag = 1
                        break
                    elif p1[x] + 1 in p1:
                        if p1[x] + 2 in p1:
                            flag = 1
                            break
                if flag == 1:
                    break
        else:
            p2.append(numbers[i])
            if len(p2) >= 3:
                p2.sort()
                for x in range(len(p2)):
                    if p2.count(x) >= 3:
                        flag = 2
                        break
                    elif p2[x] + 1 in p2:
                        if p2[x] + 2 in p2:
                            flag = 2
                            break
                if flag == 2:
                    break
    print('#%d %d' % (T, flag))