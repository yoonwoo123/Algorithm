import sys
sys.stdin = open("스도쿠_input.txt")

def make_candidate(pos):
    nums = [False] + [True for _ in range(9)]

    x = (pos[0]//3) * 3
    y = (pos[1]//3) * 3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if puzzle[i][j]:
                nums[puzzle[i][j]] = False

    for i in range(9):
        if puzzle[pos[0]][i]:
            nums[puzzle[pos[0]][i]] = False
        if puzzle[i][pos[1]]:
            nums[puzzle[i][pos[1]]] = False

    return [i for i, e in enumerate(nums) if e]

def backtracking(k):
    global state
    if k == len(zero_position):
        # print('출력문')
        for e in puzzle:
            print(' '.join(list(map(str, e))))
        state = True
    else:
        for num in make_candidate(zero_position[k]):
            puzzle[zero_position[k][0]][zero_position[k][1]] = num
            backtracking(k+1)
            if state:
                break
            puzzle[zero_position[k][0]][zero_position[k][1]] = 0

puzzle = []
zero_position = []
state = False
a = []
for i in range(9):
    row = list(map(int, input().split()))
    puzzle.append(row)
    for j in range(9):
        if not row[j]:
            zero_position.append([i, j])

backtracking(0)
