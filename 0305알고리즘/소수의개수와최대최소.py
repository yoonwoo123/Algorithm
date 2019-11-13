import sys
sys.stdin = open("소수의개수와최대최소_input.txt")

N = list(map(int, input().split()))
# 소수는 일단 무조건 홀수 ( 짝수는 2 외에는 절대 될 수 없다. )
# 소수는 나누었을 때 1과 자기자신뿐
prime = []
for x in range(min(N), max(N)+ 1): #a 부터 b까지 수를 전부 검사
    flag = 0
    if x != 1 and x % 2 == 1 or x == 2: # 2를 제외한 짝수를 걸러줌
        for i in range(3, int(x**0.5) + 1): # 3부터 제곱근까지의 숫자만 검사해도ok
            if x % i == 0: # 나누고 나머지가 0이아니면 소수가아님
                flag = i
                break
        if flag == 0:
            prime.append(x)
print(len(prime))
print(min(prime)+max(prime))