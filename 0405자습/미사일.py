import sys, copy
sys.stdin = open("미사일_input.txt")
# 미사일은 배에 맞았을 때만 효력이 발생하므로
# 미사일을 쏠 수 있는 좌표는 배의 좌표뿐이다.
# 미사일을 배에 쏘는 경우의 수는 중복순열이다. (1,1,1), (1,1,2) ...
# 단 에너지가 0이 된 배는 쏠 필요가 없다.

# 모든 경우의수에서 배가 가장 많이 침몰시킬때의 개수를 구해라

def perm(no):
    global my_max
    if no >= bomb: # 폭탄을 전부 쏘면
        # print(a)
        cnt = 0
        for i in range(bomb): # 폭탄개수만큼
            if arr[a[i]][2] > 0: # 배가 침몰 즉 에너지가 0 이하가 되면 미사일 쏴도 안터져야함
                for j in range(N): # 폭탄이 터질때 데미지입을 배 선택
                    if d[a[i]][j] == 1:
                        arr[j][2] -= damage # [j][2] 그 배의 에너지를 데미지만큼감소

        for i in range(N): # 배 갯수만큼
            if arr[i][2] <= 0: # 배 에너지가 0이하인것들
                cnt += 1

        if my_max < cnt: # 최대갯수구하기
            my_max = cnt

        for x in range(N): # 원본으로 복구
            for y in range(3):
                arr[x][y] = ori[x][y]
        # arr = copy.deepcopy(ori)
        # print(my_max)
        return

    for i in range(N): # boat중 0번째, 1번째 보트
        a[no] = i
        perm(no + 1)

N = int(input())
my_max = -1

arr = [] # arr = [보트좌표x, y, 에너지]
for i in range(N):
    # X, Y, E = map(int, input().split())
    arr.append(list(map(int, input().split())))

ori = copy.deepcopy(arr)
# print(ori)
bomb, damage, darea = map(int, input().split())
a = [0] * bomb
d = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N): # 미사일이 0번에 떨어지면
    bx = arr[i][0]
    by = arr[i][1]
    for j in range(N): # 주위 배와의 거리계산
         if darea >= abs(bx - arr[j][0]) + abs(by - arr[j][1]):
             d[i][j] = 1 # 1이면 데미지를 입는다.
# print(d)
perm(0)
print(N - my_max)