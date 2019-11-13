import sys
sys.stdin = open("카카오5_input.txt")

stones = list(map(int, input().split()))
k = int(input())

answer = 0
LS = len(stones)

mston = sorted(stones, reverse=True)

print(mston)
flag = 1
while flag:
    zcnt = 0
    mymin = 200000001
    for i in range(LS):
        if mymin > stones[i] > 0:
            mymin = stones[i] # 최솟값 찾자
        if stones[i] == 0:
            zcnt += 1
            if zcnt == k:
                flag = 0
                print(answer)  # return 0
                break
        else:
            zcnt = 0

    # 위에서 리턴이 안됐으므로 최솟값 찾았고 이상없는돌다리
    # 일단 최솟값만큼의 인원은 돌수있는것. 모든 돌다리에서
    # 최솟값만큼씩 빼고 시작하자
    answer += mymin
    for i in range(LS):
        if stones[i] >= mymin:
            stones[i] -= mymin
        else:
            stones[i] = 0

# flag = 1
# while flag:
#     # 여기서부터 진정 돌다리건너며 빼고 계산
#     zcnt = 0
#     for i in range(LS):
#         if stones[i] == 0:
#             zcnt += 1
#             if zcnt == k:
#                 flag = 0
#                 print(answer) # return answer
#                 break
#             continue
#         else:
#             stones[i] -= 1
#             zcnt = 0
#     # 잘 건너서 for문을 빠져나온다면
#     answer += 1
