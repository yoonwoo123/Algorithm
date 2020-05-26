import itertools

def chk(arr):
    diag1 = diag2 = 0
    for i in range(3):
        row = col = 0
        diag1 += arr[i][i]
        diag2 += arr[i][2-i]
        for j in range(3):
            row += arr[i][j]
            col += arr[j][i]
        if row != 15 or col != 15: return False
    if diag1 != 15 or diag2 != 15: return False
    return True

ans = 100
use_two = [1, 3, 7, 9] # 1과 9 3과 7은 세트
use_thr = [2, 4, 6, 8]

arr = [[0 for _ in range(3)] for q in range(3)]
arr[1][1] = 5

for perm_thr in itertools.permutations(use_thr, 4):
    for perm_two in itertools.permutations(use_two, 4):
        arr[0][0], arr[0][2], arr[2][0], arr[2][2] = perm_thr
        arr[0][1], arr[1][0], arr[1][2], arr[2][1] = perm_two
        if chk(arr):
            tot = 0
            for i in range(3):
                for j in range(3):
                    tot += abs(arr[i][j] - s[i][j])
            ans = min(ans, tot)
print(ans)
