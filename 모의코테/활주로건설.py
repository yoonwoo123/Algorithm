import sys, copy, time, collections
sys.stdin = open("활주로건설_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, X = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    tot = 0

    for x in range(N):
        flag = 1
        chk = [0] * 7  # 0~6체크박스용
        pre = table[x][0] # 현재 찍고 있는 높이 (가장 첫 값)
        chk[pre] += 1 # 첫값 체크값 + 1
        for y in range(1, N): # 2번째 칸 부터 확인
            if pre < table[x][y]:
                if flag == 0 or table[x][y] - pre >= 2:
                    flag = 0
                    break
                if chk[pre] < X:
                    flag = 0
                    break
                chk[pre] = 0 # 둘다 통과하면 체크한 프리값 0으로
                pre = table[x][y] # pre 값을 지금만난값으로
                chk[pre] += 1 # 지금만난값 카운트 1 증가

            elif pre > table[x][y]:
                if flag == 0 or pre - table[x][y] >= 2:
                    flag = 0
                    break
                chk[pre] = 0 # 체크해둔값 초기화
                pre = table[x][y]
                chk[pre] += 1
                flag = 0 # 이 플래그가 1이 되려면 이 값이 커져야

            else: # 두 값이 같을 때
                chk[pre] += 1 # 찍어놓은 값 카운트 +1
                if flag == 0 and chk[pre] >= X:
                    flag = 1
                    chk[pre] = 0 # 체크해둔값 초기화
        if flag: # 플래그가 1이면
            tot += 1

    for y in range(N):
        flag = 1
        chk = [0] * 7  # 0~6체크박스용
        pre = table[0][y] # 현재 찍고 있는 높이 (가장 첫 값)
        chk[pre] += 1 # 첫값 체크값 + 1
        for x in range(1, N): # 2번째 칸 부터 확인
            if pre < table[x][y]:
                if flag == 0 or table[x][y] - pre >= 2:
                    flag = 0
                    break
                if chk[pre] < X:
                    flag = 0
                    break
                chk[pre] = 0 # 둘다 통과하면 체크한 프리값 0으로
                pre = table[x][y] # pre 값을 지금만난값으로
                chk[pre] += 1 # 지금만난값 카운트 1 증가

            elif pre > table[x][y]:
                if flag == 0 or pre - table[x][y] >= 2:
                    flag = 0
                    break
                chk[pre] = 0 # 체크해둔값 초기화
                pre = table[x][y]
                chk[pre] += 1
                flag = 0 # 이 플래그가 1이 되려면 이 값이 커져야

            else: # 두 값이 같을 때
                chk[pre] += 1 # 찍어놓은 값 카운트 +1
                if flag == 0 and chk[pre] >= X:
                    flag = 1
                    chk[pre] = 0 # 체크해둔값 초기화
        if flag: # 플래그가 1이면
            tot += 1

    print(f'#{T} {tot}')
