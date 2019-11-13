# import sys
# sys.stdin = open("이차원_input.txt")
#
# R, C, K = map(int, input().split())
# # table[R][C] == K 가 됐을 때 걸린 시간의 최소값 구하기
# # 행과 열 크기가 100이 넘어가면 버리고 시간이 100이 넘어가면 -1 출력
#
# table = [list(map(int, input().split())) for _ in range(3)]
# ntable = []
# ncnt = [0] * 10 # 1~9 까지 카운트 예정
#
# xlen = len(table)
# ylen = len(table[0])
#
# if xlen < ylen:
#     # 열 연산
# else:
#     # 행 연산
#     for x in range(xlen):
#         for y in range(ylen):
#             ncnt[table[x][y]] += 1
#         for i, v in enumerate(ncnt):
w = [[5, 0, 1], [2, 2, 2], [1, 3, 3], [1, 4, 4], [1, 6, 5]]
# w = sorted(w)
# w.sort()
print(w)