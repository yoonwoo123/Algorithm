import sys
sys.stdin = open("오픈채팅방_input.txt")

record = []
for i in range(5):
    record.append(input())

# 채팅방에 나간 유저가 닉네임을 변경하는 일은 일어나지 않는다.
# 즉 Change 명령은 채팅방에 있는 사람것만 나온다.

answer = []
ids = {} # id가 key, 닉네임이 value
for re in record:
    if re[0] == 'E':
        cin = re.split() # command, id, nickname
        ids[cin[1]] = cin[2]
        answer.append([cin[1], 1]) # 1 들어왔습니다 0 나갔습니다.
    elif re[0] == 'L':
        cin = re.split()  # command, id
        answer.append([cin[1], 0])

    else: # C
        cin = re.split()  # command, id, nickname
        ids[cin[1]] = cin[2]

LA = len(answer)

for i in range(LA):
    id = answer[i][0]
    state = answer[i][1] # 1은 들어왔습니다 0은 나갔습니다
    if state:
        answer[i] = f'{ids[id]}님이 들어왔습니다.'
    else:
        answer[i] = f'{ids[id]}님이 나갔습니다.'
print(answer)