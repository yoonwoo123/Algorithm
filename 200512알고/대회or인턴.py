import sys
sys.stdin = open("대회or인턴_input.txt")

# 여학생은 남학생의 2배가 대회에 참여해야 한다.
# K명은 전체인원에서 무조건 빼야 한다.

# 즉 N // 2와 M을 비교해서 더 작은 인원에 맞춰 팀을 만들 수 있다.
# 더 큰 쪽은 작은 인원에 맞춰 뺄 수 있다. 여자라면 차이 * 2 만큼 뺄 수 있다.
# 수가 같아질 때까지 빼도 K를 충족하지 못하면 더 빼야하므로 여자는 2씩 남자는 1씩 빼며
# 최대팀원 수를 리턴하자.

N, M, K = map(int, input().split()) # 여, 남

answer = 0
while K > 0:
    if N // 2 > M:
        K -= (N // 2 - M) * 2
        N -= (N // 2 - M) * 2
    elif N // 2 < M:
        K -= M - N // 2
        M -= M - N // 2
    else:
        N -= (K // 3) * 2
        M -= K // 3
        K %= 3
        break
if K <= 0:
    answer = min(N // 2, M)
elif K == 1:
    answer = min((N - 1) // 2, M)
elif K == 2:
    answer = min((N - 2) // 2, M)
print(answer)