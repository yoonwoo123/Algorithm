import sys
sys.stdin = open("타일장식물_input.txt")

N = int(input())

arr = [1, 1]

# 78 번 for문을 돌리면 길이 80의 원하는 배열을 구한다.
for i in range(78):
    arr.append(arr[i] + arr[i+1])
answer = 2 * (arr[N-1] + arr[N])
print(answer)