import sys
sys.stdin = open("보물상자_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, K = map(int, input().split())
    arr = list(input())
    # N은 항상 4의 배수이므로 N // 4 로 나누어서 그룹지어야한다.
    # 도는 순서는 맨 뒤에 있는 것이 맨 앞으로 가면 됨.
    # N // 4 회전 만큼하면 원상태로 돌아옴

    nums = []
    sixteen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    gro = []

    for i in range(4):
        # if ''.join(arr[(N//4) * i : (N//4) * (i+1)]) not in nums:
        nums.append(''.join(arr[(N//4) * i : (N//4) * (i+1)]))

    # 3개씩 잘리는데 이것은 N // 4 이다.
    for i in range(N//4 - 1):
        arr.insert(0, arr.pop(-1)) # 시계방향회전
        for i in range(4):
            if ''.join(arr[(N // 4) * i: (N // 4) * (i + 1)]) not in nums:
                nums.append(''.join(arr[(N // 4) * i: (N // 4) * (i + 1)]))
    # print(nums)

    for i in range(16):
        for num in nums:
            if num[0] == sixteen[-(i+1)]:
                gro.append(num)
    flag = 1
    while flag:
        flag = 0
        for x in range(len(gro) - 1):
            if sixteen.index(gro[x][0]) == sixteen.index(gro[x + 1][0]):
                for i in range(1, N//4):
                    # if gro[-1][x] == num[x]:
                    if sixteen.index(gro[x][i]) == sixteen.index(gro[x+1][i]):
                        continue
                    if sixteen.index(gro[x][i]) < sixteen.index(gro[x+1][i]):  # 정렬되있는마지막수 vs 정렬중인 수
                        gro[x], gro[x+1] = gro[x+1], gro[x]
                        flag = 1
                        break
                    else:
                        break

    # print(gro)
    # print(gro[K-1])
    tar = list(gro[K-1])
    res = 0
    for i in range(1, N//4 + 1):
        res += sixteen.index(tar[-i]) * (16 ** (i-1))
    print(f'#{T} {res}')
