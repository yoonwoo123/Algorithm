import sys
sys.stdin = open("조이스틱_input.txt")

name = input()

answer = 0
alphas = [x for x in range(14)]
tmp = [x for x in range(12, 0, -1)]
alphas.extend(tmp)
# print(alphas)
zeros = []
N = len(name)
nuname = [0] * N
cnt = 0
nuname[0] = alphas[ord(name[0]) - 65]
for i in range(1, N):
    nuname[i] = alphas[ord(name[i]) -65]
    if nuname[i] == 0:
       cnt += 1
    elif nuname[i] != 0 and cnt != 0:
        zeros.append(cnt)
print(nuname)
print(zeros)
s = sum(nuname)
if zeros == []:
    print(s + N - 1)

blank = [0] * N
blank[0] = nuname[0]

cnt = 0 # zeros의 인덱스
ccnt = 0 # 값을 바꾼 횟수
flag = 1
for i in range(1, N):
    if nuname[i] == 0 and flag:
        flag = 0  # 0 을 만남
        if i - 1 >= zeros[cnt]: # 그냥 직진이 더 낫다.
            cnt += 1
            ccnt += 1
        else: # 돌아가는게 더 낫다.
            print(s + ((i - 1) * 2) + N - (i+zeros[cnt]))
            break
    elif nuname[i] == 0 and flag == 0:
        ccnt += 1
    else:
        blank[i] = nuname[i] # 값을 바꿔주고
        ccnt += 1 # 바꿔준 조작횟수를 1늘려줌
        flag = 1 # flag 다시 초기화

    if nuname == blank:
        print(s + ccnt)
        break
# answer += alphas[ord(name[0]) - 65] # 맨 처음꺼는 미리 더해주고 시작하자


# for i in range(N-1):
# # i = 0
# # while True:
#     if ori[i+1] != name[i+1]: # 즉 A가 아니면
#         ori[i+1] = name[i+1]
#         answer += alphas[ord(name[i+1]) - 65]
#         answer += 1 # 한칸 넘어가는 용도
#     if ori[i]