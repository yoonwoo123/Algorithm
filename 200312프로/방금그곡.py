import sys, re
sys.stdin = open("방금그곡_input.txt")

m = input()
musicinfos = list(input().split())

answer = ''
sol = [0, 'sol']
m = m.replace('A#','H');
m = m.replace('C#','I');
m = m.replace('D#','J');
m = m.replace('F#','K');
m = m.replace('G#','L');
my_dict = dict()

for musicinfo in musicinfos:
    p = musicinfo.split(',')
    ptime = (int(p[1][0:2]) * 60 + int(p[1][3:5])) - (int(p[0][0:2]) * 60 + int(p[0][3:5]))
    title = p[2]
    melody = p[3]
    melody = melody.replace('A#', 'H');
    melody = melody.replace('C#', 'I');
    melody = melody.replace('D#', 'J');
    melody = melody.replace('F#', 'K');
    melody = melody.replace('G#', 'L');
    n, r = divmod(ptime, len(melody))
    melody = melody * n + melody[0:r]

    if m in melody:
        if sol[0] < ptime:
            sol[0], sol[1] = ptime, title

if sol == [0, 'sol']:
    print('(None)')
else:
    print(sol[1])