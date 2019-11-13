def powerset(n, k, my_sum): # n :원소의 갯수, k : 현재 depth
    global count, total
    if my_sum > 10: return
    total += 1
    if n == k:
    #     my_sum = 0
    #     for i in range(n): # 각 부분 배열의 원소 출력
    #         if A[i] == 1:
    #             my_sum += data[i]
        if my_sum == 10:
            count += 1
            print("%d: " % (count), end="")
            for i in range(n):  # 각 부분 배열의 원소 출력
                if A[i] == 1:
                    print("%d " % data[i], end="")
            print()
    else:
        A[k] = 1 # k번 요소 o 숫자가 들어갈때만 그 데이터를 더해주므로 data[k]를 더해준다.
        powerset(n, k + 1, my_sum + data[k]) # 다음 요소 포함 여부 결정
        A[k] = 0 # k번 요소 x
        powerset(n, k + 1, my_sum) # 원래대로 돌리려면 더해준것을 없애야하므로 my_sum만

total = 0
count = 0
N = 10
A = [0] * N
# data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset(N, 0, 0)
print('돌아간 횟수: %d' % total)