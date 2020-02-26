import sys
sys.stdin = open("비밀지도_input.txt")

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = []
for i,j in zip(arr1,arr2):
    a12 = str(bin(i|j)[2:])
    a12=a12.rjust(n,'0')
    a12=a12.replace('1','#')
    a12=a12.replace('0',' ')
    answer.append(a12)
print(answer)