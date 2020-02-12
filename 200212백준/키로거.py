import sys, collections
sys.stdin = open("키로거_input.txt")
input = sys.stdin.readline

# tc = int(input())
# for T in range(1, tc+1):
#     L = input().strip()
#     cursor = 0 # 커서의 위치
#     link = [[1, "head", 1], [0, "tail", 0]] # 머리와 꼬리 선언
#     linkidx = 2 # 링크배열의 총 길이 겸 방금 들어온 새노드의 인덱스
#     # 이전노드 번호, 값, 다음노드 번호
#     for char in L: # i = L의 인덱스
#         if char == '<':
#             if link[cursor][0] != 0 and link[cursor][0] != 1:
#                 cursor = link[cursor][0]
#         elif char == '>':
#             if link[cursor][0] != 0 and link[cursor][2] != 1:
#                 cursor = link[cursor][2]
#         elif char == '-':
#             link[link[cursor][0]][2] = link[cursor][2]
#             link[link[cursor][2]][0] = link[cursor][0]
#             cursor = link[cursor][0]
#         else:
#             link.append([cursor, char, link[cursor][2]]) # 이전노드, 값,
#             # 다음 노드 번호(앞의 노드가 가리키는것을 내가 가리킴)
#             link[link[cursor][2]][0] = linkidx # 뒷 노드의 전노드가 나
#             link[cursor][2] = linkidx # 앞 노드가 나를 가리키도록
#             linkidx += 1 # 링크인덱스를 1 증가
#             cursor = link[cursor][2]
#     answer = ''
#     start = link[0][2]
#     while True:
#         if start == 1: break
#         answer += link[start][1]
#         start = link[start][2]
#     print(answer)

def find_pwd(x):
    left = []
    right = []
    for i in p:
        if i == '<':
            if not left:
                continue
            else:
                right.append(left.pop())
        elif i == '>':
            if not right:
                continue
            else:
                left.append(right.pop())
        elif i == '-':
            if not left:
                continue
            else:
                left.pop()
        else:
            left.append(i)
    for _ in range(len(right)):
        left.append(right.pop())
    return left


if __name__ == "__main__":
    n = input()

    for i in range(int(n)):
        p = list(input().strip())
        print(''.join(find_pwd(p)))