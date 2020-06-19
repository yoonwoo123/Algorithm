import sys, itertools

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

def solution(baseball):

    def DFS(tmp, chk):

        if len(tmp) == 3:
            arr.append(''.join(map(str, tmp))) # str으로 저장
            return

        for i in range(1, 10):
            if chk[i]: continue
            chk[i] = 1
            tmp.append(i)
            DFS(tmp, chk)
            chk[i] = 0
            tmp.pop()

    answer = 0
    arr = [] # 모든 경우의 수
    DFS([], [0 for x in range(11)])
    # 상위 for문과 하위 for문을 바꾼 후에
    # 상위 for문은 뒤로부터 탐색하고 pop을 뒤부터 하면
    # 인덱스에러가 안난다. pop 후에 바로 break
    for nums, strike, ball in baseball:
        delete = []
        nums = str(nums)
        for k in range(len(arr)):
            scnt, bcnt = 0, 0
            for i in range(len(arr[k])):
                if nums[i] == arr[k][i]:
                    scnt += 1
                elif nums[i] in arr[k]:
                    bcnt += 1
            if strike != scnt or ball != bcnt:
                delete.append(k)
        for i in range(len(delete)):
            arr.pop(delete[i] - i)

    # print(arr)
    return len(arr)

print(solution(baseball))