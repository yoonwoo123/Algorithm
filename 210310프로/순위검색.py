import itertools

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    division = {'cpp': 0, 'java': 0, 'python': 0, 'backend': 1, 'frontend': 1, 'junior': 2, 'senior': 2, 'pizza': 3, 'chicken': 3}
    type = {}

    for inf in info:
        inf = inf.split(' ')
        score = int(inf.pop())
        for i in range(5):
            for comb in itertools.combinations(inf, i):
                newInfo = ['-' for _ in range(4)]
                for tag in comb:
                    newInfo[division[tag]] = tag

                key = ''.join(newInfo)
                if key not in type:
                    type[key] = [score]
                else:
                    type[key].append(score)

    for v in type.values():
        v.sort(reverse=True)

    for q in query:
        q = q.split(' ')
        score = int(q.pop())
        q = ''.join(q).split('and')
        q = ''.join(q)

        if q not in type:
            answer.append(0)
        else:
            left = 0
            right = len(type[q])

            while left < right:
                mid = (left + right) // 2
                if score <= type[q][mid]:
                    left = mid + 1
                else:
                    right = mid

            answer.append(left)

    return answer

print(solution(info, query))