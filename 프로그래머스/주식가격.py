import sys
sys.stdin = open("주식가격_input.txt")

prices = list(map(int, input().split()))

answer = []
N = len(prices)

chk = [0] * (max(prices)+1) # 한번도 떨어져보지 않은 값을 체크해준다.

for i in range(N):
    if chk[prices[i]] == 0:
        cnt = 1
        flag = 1
        for j in range(i+1, N):
            if prices[i] <= prices[j]:
                cnt += 1
            elif prices[i] > prices[j]:
                answer.append(cnt)
                flag = 0
                break

        if flag:
            chk[prices[i]] = 1
            answer.append((N - 1) - i)
    else:
        answer.append((N - 1) - i)
print(answer)