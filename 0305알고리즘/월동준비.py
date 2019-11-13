import sys
sys.stdin = open('월동준비_input.txt')

N = int(input())
dotoris = list(map(int, input().split()))
# print(dotoris)
idi_sum = 0
# idi_branch = []
idi_max = 0
gen_sum = 0
for dotori in dotoris:
    if dotori > 0:
        gen_sum += dotori
    # idi 다람쥐
    if idi_sum == 0 and dotori > 0: # 젤처음도토리
        idi_sum += dotori
        # continue
    else:
        idi_sum += dotori
    if idi_max < idi_sum:
        idi_max = idi_sum
    elif idi_sum < 0: # 만약 최대값이 0인 케이스라면? 그래서 0은 계속하기로.
        idi_sum = 0

    elif max(dotoris) < 0:
        gen_sum = max(dotoris)
        idi_max = max(dotoris)

    # gen 다람쥐
# for dotori in dotoris:
#     if dotori > 0:
#         gen_sum += dotori
#     elif max(dotoris) < 0: # 도토리가 전부 음수일땐 1개만먹는게최대값
#         gen_sum += max(dotoris)
#         break
print("%d %d" % (idi_max, gen_sum))