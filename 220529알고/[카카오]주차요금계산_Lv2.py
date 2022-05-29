import math

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees, records):

    # 시간을 분단위로 변경 (x60)한 후에 몇 분동안 있었는지 계산하자.
    # 입차가 있고 출차가 없다면 모두 23:59분에서 빼준걸로 계산해주자.
    # 정수로 나누어떨어지지 않으면 올림하여 계산
    # 기본시간 이하인 것은 기본요금으로 청구
    # 차량번호가 작은 순으로 answer에 금액을 넣어 반환한다.

    answer = []
    defaultTime, defaultFee, moreTime, moreFee = fees
    maxTime = 23 * 60 + 59
    carLogs = {} # IN 시간을 저장하는 딕셔너리
    cars = {} # 있었던 시간을 기록하는 딕셔너리

    for record in records:
        time, carNumber, action = record.split(" ")
        time = list(map(int, time.split(":")))
        time = int(time[0]) * 60 + int(time[1])

        if action == 'IN':
            carLogs[carNumber] = time
        else:
            if carNumber in cars:
                cars[carNumber] += time - carLogs[carNumber]
            else:
                cars[carNumber] = time - carLogs[carNumber]
            carLogs.pop(carNumber)

    if len(carLogs) > 0:
        for carNumber, time in carLogs.items():
            if carNumber in cars:
                cars[carNumber] += maxTime - time
            else:
                cars[carNumber] = maxTime - time

    for carNumber in sorted(cars):
        totTime = cars[carNumber]

        if totTime <= defaultTime:
            answer.append(defaultFee)

        else:
            answer.append(math.ceil((totTime - defaultTime) / moreTime) * moreFee + defaultFee)

    return answer

print(solution(fees, records))
