import sys
sys.stdin = open("numbercard_input.txt")
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
testcases = input()
for T in range(int(testcases)):#{T+1}
    cnt = [0] * 10
    maxi = 0
    N = input()
    data = list(input())
    for i in range(len(data)):
        cnt[int(data[i])] += 1
    result = list(map(int, cnt))
    BubbleSort(result)
    for x in range(10):
        if result[-1] == cnt[x]:
            maxi = x
    print(f'#{T+1} {maxi} {result[-1]}')
