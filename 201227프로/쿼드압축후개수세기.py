arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

def solution(arr):

    def checkFirst(arr):
        # 처음 한번은 검증
        for x in range(N):
            for y in range(N):
                if arr[0][0] != arr[x][y]: return False
        return True

    def find(arr):
        N = len(arr)

        def quarter1(arr, N):
            number = arr[0][0]
            nextArr = []
            cnt = 0
            for x in range(0, N//2):
                tmp = []
                for y in range(0, N//2):
                    tmp.append(arr[x][y])
                    if number != arr[x][y]: cnt += 1
                nextArr.append(tmp)

            if cnt:
                return [0, nextArr]
            return [1, number]

        def quarter2(arr, N):
            number = arr[0][N//2]
            nextArr = []
            cnt = 0
            for x in range(0, N // 2):
                tmp = []
                for y in range(N // 2, N):
                    tmp.append(arr[x][y])
                    if number != arr[x][y]: cnt += 1
                nextArr.append(tmp)

            if cnt:
                return [0, nextArr]
            return [1, number]

        def quarter3(arr, N):
            number = arr[N//2][0]
            nextArr = []
            cnt = 0
            for x in range(N // 2, N):
                tmp = []
                for y in range(0, N // 2):
                    tmp.append(arr[x][y])
                    if number != arr[x][y]: cnt += 1
                nextArr.append(tmp)

            if cnt:
                return [0, nextArr]
            return [1, number]

        def quarter4(arr, N):
            number = arr[N//2][N//2]
            nextArr = []
            cnt = 0
            for x in range(N // 2, N):
                tmp = []
                for y in range(N // 2, N):
                    tmp.append(arr[x][y])
                    if number != arr[x][y]: cnt += 1
                nextArr.append(tmp)

            if cnt:
                return [0, nextArr]
            return [1, number]

        res1 = quarter1(arr, N)
        if res1[0]:
            answer[res1[1]] += 1
        else:
            find(res1[1])

        res2 = quarter2(arr, N)
        if res2[0]:
            answer[res2[1]] += 1
        else:
            find(res2[1])

        res3 = quarter3(arr, N)
        if res3[0]:
            answer[res3[1]] += 1
        else:
            find(res3[1])

        res4 = quarter4(arr, N)
        if res4[0]:
            answer[res4[1]] += 1
        else:
            find(res4[1])

    answer = [0, 0]
    N = len(arr)
    if checkFirst(arr):
        answer[arr[0][0]] = 1
        return answer

    find(arr)

    return answer

print(solution(arr))