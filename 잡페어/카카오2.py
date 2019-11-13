import sys
sys.stdin = open("카카오2_input.txt")

s = input()
cnt = 0 # cnt가 2일 때는 계속 같은 집합으로 치고 cnt가 1이 되면 그만받고 다음 배열로

answer = []
res = {}
tmp = [] # 임시저장
string = ''
for char in s:
    if char == '{':
        cnt += 1
    elif char == '}':
        if cnt == 2:
            if string != '':
                tmp.append(int(string))
                string = ''
            res[len(tmp)] = tmp
            tmp = []
            cnt -= 1
    elif char == ',':
        if string != '':
            tmp.append(int(string))
            string = ''
    else: # 숫자들
        if cnt == 2:
            string += char
            # tmp.append(int(char))
# print(res)
LR = len(res)

for i in range(1, LR+1):
    for num in res[i]:
        if num not in answer:
            answer.append(num)
            break
print(answer)