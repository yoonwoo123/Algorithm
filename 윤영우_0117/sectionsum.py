import sys
sys.stdin = open("sectionsum_input.txt")
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
testcases = input()
for T in range(int(testcases)):#{T+1}
    NM = input()
    NandM = list(map(int, NM.split()))
    N = NandM[0]
    M = NandM[1]
    #NandM[0] = N , NandM[1] = M
    data = list(map(int, input().split()))
    total = []

    for i in range(N-M+1): # N-M번 반복
        sum = 0
        for x in range(M):
            sum += data[i+x]
        total.append(sum)
        BubbleSort(total)
    result = total[-1] - total[0]
    print(f'#{T+1} {result}')