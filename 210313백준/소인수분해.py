N = 9991

# N이 소수인지 아닌지 판별하면서 소수가 아니라 나눠지는 수는 출력하고
# 나머지 값으로 계속해서 이어간다. 소수인 값이 나오면 자기 자신을 출력한다.
def primeFac(N):
    flag = 1
    while flag:
        flag = 0
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                print(i)
                N //= i
                flag = 1
                break
    if N != 1:
        print(N)

if N != 1:
    primeFac(N)
