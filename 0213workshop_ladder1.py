import sys
sys.stdin = open("0213workshop_ladder1_input.txt")
testcases = 10
for T in range(testcases):
    N = input()
    ladder = []
    for i in range(100):
        tmp = list(map(int, (input().split())))
        ladder.append(tmp)
    # print(ladder)
    start = 0
    for x in range(100):
        if ladder[99][x] == 2:
            print(x)
            place = x
            break

    # 0. 시작하자마자 좌우에 1이 나올수도 있으므로 먼저 체크하자
    # 1. start에서 1칸씩 위로 올라가면서 내 좌우가 1인가 확인
    # 2. 좌 또는 우가 1이 나오면 1이 나온 방향(ex 좌) 로 계속 가면서
    # 3. 좌로 가는 곳이 1인지 확인해서 1일 때만 움직임
    # 4. 1이 아닌 경우 다시 위로 올라가게 하고 위로 올라가면서 또 좌우가1인지 확인

    # 마지막인지 즉 탈출했는지와 그때의 x값 어떻게 확인하지?
    #  ladder[y][x] 인데 y값이 0이 됐을때의 x값을 출력하면 된다!
    dy = [-1, 0, 0] # dy[0],dx[0]상, dy[1]좌, dy[2]우
    dx = [0, -1, 1]
    y_p = 99
    # place = ladder[99][start]
    while y_p > 0:

        if ladder[y_p][place - 1] == 1:
            place -= 1

        if ladder[y_p][place + 1] == 1:
            place += 1

        if place +1 >99 or place -1 < 0:
            y_p -= 1

        else:
            y_p -= 1