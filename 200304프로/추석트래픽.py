import sys
sys.stdin = open("추석트래픽_input.txt")

lines = [input() for _ in range(2)]

answer = 0
timetable = []
for line in lines:
    h = int(line[11:13]) * 3600 * 1000
    m = int(line[14:16]) * 60 * 1000
    s = float(line[17:23]) * 1000
    rtime = float(line[24:len(line)-1]) * 1000
    timetable.append((h + m + s - rtime + 1, h + m + s))
LT = len(timetable)
for i in range(LT):
    for t in range(2):
        stan = timetable[i][t]
        cnt = 0
        if t == 0:
            tmp = (stan - 999, stan)
        else:
            tmp = (stan, stan + 999)
        for j in range(LT):
            if tmp[0] < timetable[j][0]:
                if tmp[1] >= timetable[j][0]:
                    cnt += 1
            elif tmp[0] > timetable[j][0]:
                if tmp[0] <= timetable[j][1]:
                    cnt += 1
        answer = max(answer, cnt)
print(answer)