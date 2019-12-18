import sys, operator
sys.stdin = open("베스트앨범_input.txt")

genres = list(input().split())
plays = list(map(int, input().split()))

answer = []
L = len(plays)
g_chart = {}
totplay = {}
for i in range(L):
    genre = genres[i]
    play = plays[i]
    if genre in totplay:
        totplay[genre] += play
    else:
        totplay[genre] = play
    if genre in g_chart:
        if play in g_chart[genre]:
            g_chart[genre][play].append(i)
        else:
            g_chart[genre][play] = [i]
    else:
        g_chart[genre] = {play:[i]}
        # print(g_chart)

order = sorted(totplay.items(), key=operator.itemgetter(1), reverse=True)
# print(order[0])

for genres in order:
    genre = genres[0]
    playdes = sorted(g_chart[genre], reverse=True)
    cnt = 0 # 장르마다 최대 2개밖에 못넣는다.
    # print(playdes)
    for play in playdes:
        ids = g_chart[genre][play]
        if len(ids) > 1:
            ids.sort()
            answer.append(ids[0])
            cnt += 1
            if cnt == 2: break
            answer.append(ids[1])

        elif len(ids) == 1:
            answer.append(ids[0])
        cnt += 1
        if cnt == 2: break
        # print(ids)
print(answer)
