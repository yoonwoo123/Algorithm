import sys
sys.stdin = open("sw02_score_input.txt")
testcases = input()
for T in range(int(testcases)):
    N, K = list(map(int,input().split()))
    total = []
    tmp = []
    blank = []
    scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for _ in range(N):
        M, F, H = list(map(int, input().split()))
        total.append(M *0.35 + F *0.45 + H *0.2)
    for i in range(len(total)):
        blank.append(0)
    tmp = sorted(total)[::-1]
    tmp.append(0)
    for j in range(10):
        for i in range(len(total)):
            if total[i] > tmp[(N//10) *(j+1)] and blank[i] == 0:
                blank[i] = scores[j]
    print(f'#{T+1} {blank[K-1]}')