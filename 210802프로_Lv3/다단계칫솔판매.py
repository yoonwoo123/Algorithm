enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    def calculateMoney(name, price):
        if name == "-": return
        toMoney = int(price * 0.1)

        if toMoney < 1:
            getMoney[name] += price
        else:
            getMoney[name] += price - toMoney
            calculateMoney(companyTree[name], toMoney)

    getMoney = {name : 0 for name in enroll}
    companyTree = {}

    for i in range(len(enroll)):
        companyTree[enroll[i]] = referral[i]

    for i in range(len(seller)):
        price = amount[i] * 100
        calculateMoney(seller[i], price)

    return list(getMoney.values())

print(solution(enroll, referral, seller, amount))