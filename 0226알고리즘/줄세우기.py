import sys
sys.stdin = open('줄세우기_input.txt')

N = int(input())
order = [1]  # 1은 이미 넣어놈

order_num = list(map(int, list(input().split())))

# insert를 활용하자!
# order의 idx + 1 은 학생의 번호이다.
# 최종적으로 어떻게 줄을 섰는지 학생의 번호로 출력
# idx + 1 번째 학생이 뽑은 번호표는 order_num[idx] 이다.
# insert로 넣고 뒤집으면 끝 !


for i in range(1, len(order_num)):
    order.insert(order_num[i], i+1)
for num in order[::-1]:
    print(num, end=" ")
print()