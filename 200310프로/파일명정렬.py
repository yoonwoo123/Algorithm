import sys, re
sys.stdin = open("파일명정렬_input.txt")

files = [input() for _ in range(4)]
# files = list(input().split())
# 엄청나게 짧고 간결한 다른 분 풀이
a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
# 우선순위의 후순위부터 1순위까지 반대로 정렬을 한다.
# findall은 숫자로 된 부분을 모두 찾아서 리스트로 반환해준다. 그 중 [0] 이므로 HEAD
b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
# split()은 패턴화 시켜주는 것인데 '\d+' 를 스플릿하면 숫자를 제외한 나머지들을 그룹화한다.
print(b)

answer = []
L = len(files)
arr = []
for i in range(L):
    H = re.search('\D+', files[i]).group()
    N = re.search('\d+', files[i]).group()
    arr.append([H.lower(), int(N), i])
arr.sort()
for i in range(L):
    answer.append(files[arr[i][2]])
print(answer)