import sys
sys.stdin = open("구슬고르기_input.txt")

a = [1, 2, 3]
b = [0, 0, 0]
N = 3

def DFS(no, cnt): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
# 1] 리턴조건 : N번째이면 인쇄 후 리턴
    if no >= N:
        # if cnt == 2: # 2개만 찍고 싶을 경우 걸어주는 조건
        for i in range(cnt):
            print(b[i], end=" ")
        print()
        return
# 2] 현재 구슬을 고르기(b배열에 담기)
    b[cnt] = a[no]
    DFS(no+1, cnt+1)
# 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)
    b[cnt] = 0
    DFS(no+1, cnt)
# main ===================
DFS(0, 0)