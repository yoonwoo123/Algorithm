import sys, itertools
sys.setrecursionlimit(10**6)
sys.stdin = open("주사위윷놀이_input.txt")

def DFS(dep, horeses, tot):
    global ans
    if dep == 10:
        ans = max(ans, tot)
        return

    for i in range(4):  # i 는 움직이는 말의 번호
        course = horeses[i][0]  # 말이 위치한 코스
        if course == 4: continue # 도착한 말이라면 넘기자.
        present = horeses[i][1]  # 말의 현재 위치
        move = cmds[dep]  # 이동하는 값
        if present + move < len(table[course]):  # 이동 가능
            # 그러나 말이 이동하려는 위치에 다른 말이 있으면 이동x 때문에 확인
            for x in range(4):
                if x == i or horeses[x][0] == 4: continue
                # 코스와 위치가 같은 경우
                if horeses[x][0] == course and horeses[x][1] == present + move:
                    return
                # 말이 파란칸에 있을 경우에 겹치는 경우
                if horeses[x][1] == 0 and (present + move) % 5 == 0 and present + move < 20 and horeses[x][0] == (present + move) // 5:
                    return
                # 말이 다른 코스에 있지만 길을 공유하는 코스 1,2,3 에서 겹칠경우 !
                if course != 0 and horeses[x][0] != 0 and table[horeses[x][0]][horeses[x][1]] == table[course][present + move]:
                    if horeses[x][0] == 3 and horeses[x][1] == 0: break
                    return
                # 코스0에서 유일하게 다른 코스와 경유하는 40 에서 마주칠 경우
                if table[course][present + move] == 40 and table[horeses[x][0]][horeses[x][1]] == 40:
                    return

            if (present + move) % 5 == 0 and present + move < 20 and course == 0:  # 파랑지점 멈추면
                tmp = [horeses[i][0], horeses[i][1]]
                horeses[i][0] = (present + move) // 5  # 코스 바꿔주고
                horeses[i][1] = 0  # 말의 위치 0으로 초기화
                DFS(dep + 1, horeses, tot + table[course][present + move])
                horeses[i][0], horeses[i][1] = tmp # 원래 값으로 초기화 시켜줌
            else:
                tmp = horeses[i][1]
                horeses[i][1] = present + move
                DFS(dep + 1, horeses, tot + table[course][present + move])
                horeses[i][1] = tmp # 원래 값으로 초기화
            # else: break
        else:  # 도착 지점 도착
            tmp = horeses[i][0]
            horeses[i][0] = 4  # 도착했다고 표시
            DFS(dep + 1, horeses, tot)
            horeses[i][0] = tmp

cmds = list(map(int, input().split()))
# 인덱스가 5, 10, 15 번째 테이블에 멈추게 되면 지나가는 테이블이 바뀐다.
# 0, 1, 2, 3 순으로 원래길, 코스1, 코스2, 코스3이다.
table = [[x for x in range(0, 41, 2)], [10, 13, 16, 19, 25, 30, 35, 40], [20, 22, 24, 25, 30, 35, 40], [30, 28, 27, 26, 25, 30, 35, 40]]
ans = 0 # 최댓값을 구해야함

# 말의 상태를 0, 1, 2, 3으로 표시하여 어떤 길에 있는지 나타내자.
# 말의 상태가 4는 도착했다는 뜻
# 말이 있는 길, 위치(idx)
DFS(0, [[0, 0] for _ in range(4)], 0) # dep, horses, tot
print(ans)


# cmds = list(map(int, input().split()))
# # 인덱스가 5, 10, 15 번째 테이블에 멈추게 되면 지나가는 테이블이 바뀐다.
# # 0, 1, 2, 3 순으로 원래길, 코스1, 코스2, 코스3이다.
# table = [[x for x in range(0, 41, 2)], [10, 13, 16, 19, 25, 30, 35, 40], [20, 22, 24, 25, 30, 35, 40], [30, 28, 27, 26, 25, 30, 35, 40]]
# print(table)
#
# ans = 0 # 최댓값을 구해야함
# for prod in itertools.product((0, 1, 2, 3), repeat=10):
#     # prod는 10개의 말을 어떻게 뽑을건지 순서
#     tot = 0 # 말이 이동해서 얻은 총 점수
#     # 말의 상태를 0, 1, 2, 3으로 표시하여 어떤 길에 있는지 나타내자.
#     # 말의 상태가 4는 도착했다는 뜻
#     # 말이 있는 길, 위치(idx)
#     horeses = [[0, 0] for _ in range(4)]
#
#     for i in range(10): # 10개의 명령으로 이루어지기 때문에 고정값 10
#         target = prod[i] # 움직이는 말
#         move = cmds[i] # 이동하는 값
#         course = horeses[target][0] # 말이 위치한 코스
#         if course == 4: break
#         present = horeses[target][1] # 말의 현재 위치
#         if present + move < len(table[course]): # 이동 가능
#             # 그러나 말이 이동하려는 위치에 다른 말이 있으면 이동x 때문에 확인
#             flag = True
#             for x in range(4):
#                 if x == target: continue
#                 if horeses[x][0] == course and horeses[x][1] == present + move:
#                     flag = False
#                     break
#                 if horeses[x][1] == (present + move) % 5 and horeses[x][0] == (present + move) // 5:
#                     flag = False
#                     break
#             if flag:
#                 tot += table[course][present + move]
#                 # print(tot)
#                 if course == 0 and (present + move) % 5 == 0: # 파랑지점 멈추면
#                     horeses[target][0] = (present + move) // 5 # 코스 바꿔주고
#                     horeses[target][1] = 0 # 말의 위치 0으로 초기화
#                 else:
#                     horeses[target][1] = present + move
#             else: break
#         elif present + move >= len(table[course]): # 도착 지점 도착
#             horeses[target][0] = 4 # 도착했다고 표시
#
#     ans = max(ans, tot)
# print(ans)