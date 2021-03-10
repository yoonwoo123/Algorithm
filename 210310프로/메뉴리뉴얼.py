import itertools

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH", "CASFGW"]
course = [2,3,4]

def solution(orders, course):
    answer = []
    for i in course:
        menus = {}
        for order in orders:
            if i > len(order): continue
            for comb in itertools.combinations(order, i):
                menu = ''.join(sorted(list(comb)))
                if menu not in menus:
                    menus[menu] = 1
                else:
                    menus[menu] += 1

        mymax = 2
        newMenu = []
        for menu, cnt in menus.items():
            if cnt > mymax:
                mymax = cnt
                newMenu = [menu]
            elif cnt == mymax:
                newMenu.append(menu)

        answer.extend(newMenu)

    return sorted(answer)

print(solution(orders, course))