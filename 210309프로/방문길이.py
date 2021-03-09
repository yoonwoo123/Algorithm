# 좌표평면에서 처음가는길의 총 거리를 계산해야한다.
# 좌표의 값을 key값으로 하는 객체를 만들어서 중복체크하자.
# 경계 밖을 벗어나는 것은 무시한다.

dirs = "ULURRDLLU"

def solution(dirs):
    x, y = 0, 0
    goes = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    visited = set()

    for dir in dirs:
        nx, ny = x + goes[dir][0], y + goes[dir][1]
        if nx <= -6 or ny <= -6 or nx >= 6 or ny >= 6: continue
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        x, y = nx, ny

    return len(visited) // 2

print(solution(dirs))