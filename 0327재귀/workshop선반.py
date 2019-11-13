import sys
sys.stdin = open("선반_input.txt")

def powerset(n, k, my_sum): # n :원소의 갯수, k : 현재 depth
    global my_min
    if my_sum > my_min: return
    if n == k:
        if my_sum >= B:
            if my_min > my_sum:
                my_min = my_sum
    else:
        A[k] = 1 # k번 요소 o
        powerset(n, k + 1, my_sum+arr[k]) # 다음 요소 포함 여부 결정
        A[k] = 0 # k번 요소 x
        powerset(n, k + 1, my_sum) # 다음 요소 포함 여부 결정

tc = int(input())
for T in range(1, tc+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    A = [0 for _ in range(N)]
    my_min = 1000000000
    powerset(N, 0, 0)
    print('#%d %d' % (T, my_min - B))