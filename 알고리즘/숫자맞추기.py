import sys
sys.stdin = open('숫자맞추기_input.txt')
# 2차원으로 짭시다. 행: 플레이어 , 열 :게임
N = int(input())

# 같은 경우는 continue , 점수 획득 못하면 break
# flag 변수로 점수획득을 구분하자. flag 변수는 초기화 시점이 중요
# 이중for문시 2번쨰 for문 들가기전 flag = 0
# A 선수의 점수는 idx[0] , B = idx[1], C = idx[2]
# 얻는 점수의 총합을 구하는 문제임
# N명의 플레이어 참여 행이 플레이어
table = []
for i in range(N): # 2차원의 table 생성
    tmp = []
    tmp = list(map(int, input().split()))
    table.append(tmp)

#세로로 비교하자
my_sum = [0] * N
for x in range(3):   # 열
    my_list = []
    for y in range(N):   # 행
        my_list.append(table[y][x])
    # print(my_list)
    for i in range(N):
        if my_list.count(my_list[i]) > 1:
        # if my_list[i] in my_list:
            continue
        else:
            my_sum[i] += my_list[i]
for num in my_sum:
    print(num)
