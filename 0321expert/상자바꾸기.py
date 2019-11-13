import sys
sys.stdin = open("상자바꾸기_input.txt")

tc = int(input())
for T in range(1, tc+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for x in range(L-1, R):
            boxes[x] = i
    print('#{}'.format(T), end=" ")
    for box in boxes:
        print(box, end=" ")
    print()
# a, b = map(int, input().split())
# print(a)
# N, Q = map(int, input().split())
# print(N)