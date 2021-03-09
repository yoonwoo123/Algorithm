A, B = [5, 1, 3, 7], [2, 2, 6, 8]

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    aIndex, bIndex = 0, 0

    while bIndex < len(B):
        if A[aIndex] < B[bIndex]:
            answer += 1
            aIndex += 1
            bIndex += 1
        else:
            bIndex += 1
    return answer

print(solution(A, B))