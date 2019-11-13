import sys
sys.stdin = open("minmax_input.txt")
testcases = input()
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

for T in range(int(testcases)):#{T+1}
    N = input()
    data = list(map(int, input().split()))
    BubbleSort(data)
    result = data[len(data)-1] - data[0]
    print(f'#{T+1} {result}')
    # print(data)