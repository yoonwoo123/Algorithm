board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    s = [0]
    for move in moves:
        move -= 1
        for x in range(len(board)):
            grab = board[x][move]
            if grab:
                if s[-1] == grab:
                    s.pop()
                    answer += 2
                else:
                    s.append(grab)
                board[x][move] = 0
                break
    return answer

print(solution(board, moves))
