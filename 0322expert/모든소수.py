# import sys
# sys.stdin = open('모든소수_input.txt')

# N = list(map(int, input().split()))
N = [1, 1000000]
prime = []
for x in range(min(N), max(N)+ 1): #a 부터 b까지 수를 전부 검사
    flag = 0
    # if x % 2 == 0 and x != 2: # 2를 제외한 짝수를 걸러줌
    #     continue
    if x != 1 and x % 2 == 1 or x == 2: # 2를 제외한 짝수를 걸러줌
        for i in range(3, int(x**0.5) + 1): # 3부터 제곱근까지의 숫자만 검사해도ok
            if x % i == 0: # 나누고 나머지가 0이아니면 소수가아님
                flag = i
                break
        if flag == 0:
            print(x, end=" ")
            # prime.append(x)
# print(prime)
# print(len(prime))
# print(min(prime)+max(prime))