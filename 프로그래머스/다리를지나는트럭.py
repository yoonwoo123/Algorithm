import sys
sys.stdin = open("다리를지나는트럭_input.txt")

bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))

answer = 0
arrive = []
moving = []
wait = truck_weights
time_chk = []
while True:
    answer += 1
    if wait != []:
        if sum(moving) + wait[0] <= weight:
            moving.append(wait.pop(0))
            time_chk.append(bridge_length)

    for i in range(len(time_chk)):
        time_chk[i] -= 1
    if time_chk[0] == 0:
        arrive.append(moving.pop(0))
        time_chk.pop(0)

    if moving == [] and wait == []:
        break
answer += 1

print(answer)