import sys
sys.stdin = open("톱니바퀴_input.txt")

answer = 0
table = [list(map(int, input())) for _ in range(4)]
K = int(input())
commands = []
for _ in range(K):
    no, dir = map(int, input().split())
    commands.append((no-1, dir))

# 톱니가 맞닿아 있는 부분의 인덱스는 2, 6 자신의2와 상대6, 자신의6과 상대2
# 시계방향 회전은 insert(0, table[x].pop())
# 반시계는 table.append(table.pop(0))
                        #   0 1  1 2  2 3
# 따라서 체크해야할 톱니바퀴는 2 6  2 6  2 6 를 체크해주면 된다.
# 1 0 1 이 나오고 톱니가 정해진다면 그 톱니번호와 톱니번호-1 의 인덱스를 검사해나간다.
# 검사하는 도중 인덱스가 0보다 작거나 3보다 크면 그 부분은 빠져나가자.

# 1. 일단 검사해야할 톱니 위치에 있는 3가지 체크( 항상 commands 시작전 )

# 2. commands를 for 문으로 돌면서 명령을 수행하자.

for no, dir in commands:
    left = []
    right = []

    valid = [0] * 3  # 같으면 0 다르면 돌려야 하는 톱니이므로 1
    for i in range(3):
        if table[i][2] != table[i + 1][6]:
            valid[i] = 1
    # print(valid)
    l = no - 1
    # 왼쪽부터 체크
    for i in range(l, -1, -1):
        if valid[i] == 0: break
        left.append(i)

    for i in range(no, 3):
        if valid[i] == 0: break
        right.append(i)

    # print(left, right)

    # 이제 회전 시켜주자. no > left > right 순으로

    if dir == 1: # 시계
        table[no].insert(0, table[no].pop())
        for i in range(len(left)):
            nol = left[i]
            if i % 2 == 0:
                table[nol].append(table[nol].pop(0))
            else:
                table[nol].insert(0, table[nol].pop())

        for i in range(len(right)):
            nor = right[i] + 1
            if i % 2 == 0:
                table[nor].append(table[nor].pop(0))
            else:
                table[nor].insert(0, table[nor].pop())


    elif dir == -1: # 반시계
        table[no].append(table[no].pop(0))
        for i in range(len(left)):
            nol = left[i]
            if i % 2 == 0:
                table[nol].insert(0, table[nol].pop())
            else:
                table[nol].append(table[nol].pop(0))
        for i in range(len(right)):
            nor = right[i] + 1
            if i % 2 == 0:
                table[nor].insert(0, table[nor].pop())
            else:
                table[nor].append(table[nor].pop(0))
    # for g in table:
    #     print(g)
    # print()
for i in range(4):
    if table[i][0]:
        answer += 2 ** i
print(answer)