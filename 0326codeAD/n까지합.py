# def DFS(i):
#     global n, tot
#     if i > n:
#         return
#     tot += i
#     DFS(i+1)
#
# n = int(input())
# tot = 0
# DFS(1)
# print(tot)

# def DFS(i):
#     if i>3:
#         print() # 리턴하기전 분기점
#         return
#     print(i) # 정순으로 출력 print()를 어디에 넣냐에 따라 출력하게되는 순서다름
#     DFS(i+1)
#     print(i) # 역순으로 출력
# n = 1
# DFS(n)

def DFS(i):
    if i==3:
         # 리턴하기전 분기점
        return i
    # print(i) # 정순으로 출력 print()를 어디에 넣냐에 따라 출력하게되는 순서다름
    my_sum = DFS(i+1)
    # print(i) # 역순으로 출력
    return my_sum + i
n = 1
print(DFS(n))