import sys
sys.stdin = open("카카오4_input.txt")

k = int(input())
room_number = list(map(int, input().split()))

answer = []
room = {}
for num in room_number:
    tmp = num
    # if ratest > num:
    while True:
        if tmp in room:
            tmp += 1
        else:
            room[tmp] = 1
            ratest = tmp # 가장 최근에 배정한 방
            break

print(room)
print(list(room))

