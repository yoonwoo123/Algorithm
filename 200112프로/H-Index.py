import sys
sys.stdin = open("H-index_input.txt")

citations = list(map(int, input().split()))

answer = 0
citations.sort(reverse=True)
LenC = len(citations)
start = 0
for hidx in range(LenC, -1, -1):
    for i in range(start, LenC):
        if citations[i] >= hidx:
            start = i
            if i + 1 >= hidx >= LenC - i - 1:
                answer = hidx
                print(answer)
        else:
            break