import sys
sys.stdin = open("테트로미노_input.txt")

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 탐색 해야 할 도형의 총 개수는 19개이다 (돌린방향, 대칭 포함)
tetrominos = [[[0, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 0], [1, 0], [2, 0], [3, 0]],

              [[0, 0], [0, 1], [1, 0], [1, 1]],

              [[0, 0], [1, 0], [1, 1], [2, 1]],
              [[0, 1], [0, 2], [1, 0], [1, 1]],
              [[0, 1], [1, 1], [1, 0], [2, 0]],
              [[0, 0], [0, 1], [1, 1], [1, 2]],

              [[0, 0], [1, 0], [2, 0], [2, 1]],
              [[0, 0], [0, 1], [0, 2], [1, 0]],
              [[0, 0], [0, 1], [1, 1], [2, 1]],
              [[0, 2], [1, 0], [1, 1], [1, 2]],
              [[0, 1], [1, 1], [2, 1], [2, 0]],
              [[0, 0], [1, 0], [1, 1], [1, 2]],
              [[0, 0], [0, 1], [1, 0], [2, 0]],
              [[0, 0], [0, 1], [0, 2], [1, 2]],

              [[0, 0], [0, 1], [0, 2], [1, 1]],
              [[0, 1], [1, 1], [2, 1], [1, 0]],
              [[0, 1], [1, 0], [1, 1], [1, 2]],
              [[0, 0], [1, 0], [2, 0], [1, 1]]
              ]

max_num = 0
for tetromino in tetrominos:
    for x in range(N):
        for y in range(M):
            tot = 0
            for tx, ty in tetromino:
                if x + tx >= N or y + ty >= M: break
                tot += table[x + tx][y + ty]
            max_num = max(max_num, tot)
print(max_num)