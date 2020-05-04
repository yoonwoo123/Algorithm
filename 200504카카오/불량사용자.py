import itertools
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

def same(user, banuser):
    if len(user) != len(banuser): return False
    for i in range(len(user)):
        if banuser[i] == '*': continue
        if user[i] != banuser[i]: return False
    return True

def solution(user_id, banned_id):
    answer = 0
    # dict로 만들면 키가 전부 같을 경우를 걸러줄수 있다.
    my_dict = {}
    # idxs 는 key가 userid 이고 val이 idx 값으로 idx가 같다면 중복되는것
    idxs = {user : idx for idx, user in enumerate(user_id)}
    for perm in itertools.permutations(user_id, len(user_id)):
        print(perm)
        cnt = 0
        tmp = []
        visit = [0 for _ in range(len(perm))]
        for banuser in banned_id:
            for i in range(len(perm)):
                if same(perm[i], banuser) and visit[i] == 0:
                    tmp.append(idxs[perm[i]])
                    visit[i] = 1
                    break
        if len(tmp) == len(banned_id):
            my_dict[tuple(sorted(tmp))] = 1
    print(my_dict)
    return len(my_dict)

print(solution(user_id, banned_id))