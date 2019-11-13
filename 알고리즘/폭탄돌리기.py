import sys
sys.stdin = open('폭탄돌리기_input.txt')
K = int(input())
N = int(input())
sum_time = 0
for i in range(N):
    time, Z = input().split()
    time = int(time)
    if Z == 'T':
        sum_time += time
        if 210 <= sum_time:
            print(K)
            break
        K += 1
        if K > 8:
            K = 1
    if Z == 'F':
        sum_time += time
        if 210 <= sum_time:
            print(K)
            break
    if Z == 'P':
        sum_time += time
        if 210 <= sum_time:
            print(K)
            break
if sum_time < 210:
    print(K)