import sys
sys.stdin = open("셔틀버스_input.txt")

n, t, m = map(int, input().split())
timetable = list(input().split())

# ansh = ''
# ansm = ''
# sh, sm = 9, 0
# fh, fm = 9 + ((n-1) * t)//60, ((n-1) * t)%60
# itimetable = []
# for i in range(len(timetable)):
#     tmp = ''
#     ttime = []
#     for char in timetable[i]:
#         if char == ':':
#             ttime.append(int(tmp))
#             tmp = ''
#             continue
#         tmp += char
#     ttime.append(int(tmp))
#     itimetable.append(ttime)
# itimetable.sort()
# for cnt in range(n):
#     sh += (cnt * (t))//60
#     sm += (cnt * (t))%60
#     p = 0
#     for hour, min in itimetable:
#         if sh > hour or (sh == hour and sm >= min):
#             p += 1
#             if sh == fh and sm == fm and p == m:
#                 ansh = itimetable[m-1][0]
#                 ansm = itimetable[m-1][1] - 1
#                 if ansm < 0:
#                     ansm += 60
#                     ansh -= 1
#                 break
#             elif p == m: break
#     for q in range(p):
#         itimetable.pop(0)
#     print(itimetable)
# if ansh == '' and ansm == '':
#     if fh < 9:
#         answer = '09:00'
#     else:
#         fh, fm = str(fh), str(fm)
#         fh, fm = fh.rjust(2, '0'), fm.rjust(2, '0')
#         answer = fh + ':' + fm
# else:
#     ansh, ansm = str(ansh), str(ansm)
#     ansh, ansm = ansh.rjust(2, '0'), ansm.rjust(2, '0')
#     answer = ansh + ':' + ansm
# print(answer)

def solution(n, t, m, timetable):
    answer = ''
    timetable = [ int(time[:2])*60 + int(time[3:5]) for time in timetable ]
    timetable.sort()
    last_time = 540 + (n - 1) * t
    for i in range(n):
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n - 1:
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            time = timetable[m - 1] - 1
            return '%02d:%02d' % (time // 60, time % 60)
        for j in range(m-1, -1, -1):
            bus_arrive = 540 + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]

print(solution(n, t, m, timetable))