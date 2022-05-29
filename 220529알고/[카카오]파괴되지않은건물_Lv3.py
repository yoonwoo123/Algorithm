
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

def solution(board, skill):
    # 정확성, 효율성 문제 -> 이중for문을 통해 정확성은 Allpass
        # 허나 효율성은 어떻게 해야할까.. 좌표값별로 저장?
        # 시간복잡도 = 100만 x 25만
        # 25만번은 무조건 돌아야 하는 것이다.
        # 100만번의 경우 전부 돌지 않고 좌표값만으로 직사각형의
        # 범위를 표기할 방법을 찾아보자. NxM이 아닌 상수로 줄이는 아이디어
        # 직사각형의 네 꼭짓점에만 값을 적어보자. 25만 X 4 = 100만번

        # 해설을 보니 누적합을 이용해서 푸는 문제였다...
        # 엄청난 아이디어성 해결방법..

    # type == 1 이면 공격 -degree
    # type == 2 이면 회복 +degree
    # type, 행1, 열1, 행2, 열2, degree

    answer = 0
    checkBoard = [[[] for x in range(len(board[0]))] for w in range(len(board))]

    for g in checkBoard:
        print(g)
    print()
    cnt = 1

    for type, r1, c1, r2, c2, degree in skill:
        posSet = set()
        posSet.add((r1, c1))
        posSet.add((r1, c2))
        posSet.add((r2, c1))
        posSet.add((r2, c2))

        if type == 1:
            for r, c in posSet:
                checkBoard[r][c].append([cnt, -degree])
        else:
            for r, c in posSet:
                checkBoard[r][c].append([cnt, degree])

        cnt += 1

    for g in board:
        print(g)
    print()

    for g in checkBoard:
        print(g)
    print()

    # for x in range(len(board)):
    #     for y in range(len(board[x])):
    #         if board[x][y] > 0:
    #             answer += 1

    return answer

print(solution(board, skill))

