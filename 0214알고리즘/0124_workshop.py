import sys
sys.stdin = open("0124_workshop_input.txt")
testcases = input()

for T in range(int(testcases)):
    no = int(input()) # 금속막대 개수
    data = list(map(int, input().split()))
    male = []
    female = []
    screws = []
    result = []
    for i in range(no * 2):
        if i % 2 == 0:
            male.append(data[i])
        else:
            female.append(data[i])

    for i in range(len(data)):
        if i % 2 == 0:
            tmp = []
            tmp.append(data[i])
            tmp.append(data[i+1])
            screws.append(tmp)
    #print(screws)
    for i in range(len(data)//2):
        if screws[i][0] in male and screws[i][0] not in female:
            result.append(screws[i])
    #print(result)
    cnt = 0
    while len(result) < len(screws):
        if result[-1][1] == screws[cnt][0]:
            result.append(screws[cnt])
            cnt = 0
        else:
            cnt += 1
    print(f'#{T+1}', end=' ')
    for i in range(len(data)//2):
        print(' '.join(map(str, result[i])), end=' ')
    print()
    #print(screws)
    # def replay(m): # input 넣어줘야함
    #     for i in range(len(male)):
    #         if m == male[i]:
    #             print(male[i], end=" ")
    #             print(female[i], end=" ")
    #             m = female[i]
    #             replay(m)

    # for i in range(no * 2):
    #     #if i % 2 == 0 and data[i] not in female:
    #     if data[i] in male and data[i] not in female:
            #print(male[i//2], end=" ") # 처음 들어가는 숫나사 번호
    #         first = i
    #         # print(female[i//2], end=" ")
    #         # for x in range(len(male)):
    #         #     if male[x] == female[i//2]:
    #         #         print(male[x], end=" ")
    #         #         print(female[x], end=" ")
    #         #     if female[x] == male[p]
    #         # print(data[i], end=" ") # 처음 들어가는 숫나사 번호
    #         # print(data[i+1], end=" ")
    # # print(male[first//2], end=" ")
    # # print(female[first//2], end=" ")
    # m = first//2+1
    # replay(m)
