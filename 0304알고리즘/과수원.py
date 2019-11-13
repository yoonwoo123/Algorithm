import sys
sys.stdin = open("과수원_input.txt")

N = int(input())
table = []

for i in range(N):
    table.append(list(map(int, input())))

# 함수 하나를 만들어서 계속 활용 (좌표값을 입력받아 그 안의 수를 검사하는것)
# 4 사분면을 쪼개서 좌표값을 입력받아 각 사분면의 사과의개수를 맞춰보자
# 4개의 사분면이 전부 같으면 res += 1 해서 최종적으로 res를 출력하자.
# res = 0 이면 -1을 출력

