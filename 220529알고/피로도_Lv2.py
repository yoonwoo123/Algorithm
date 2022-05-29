
k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(k, dungeons):
    global answer
    # 스케줄링 문제인것 같다.
    # 피로도가 많을 때 최소 필요 피로도가 높은 곳을 들어가야 유리할 것이다.
    # 또한 같은 최소 필요 피로도라 했을 때 피로도 소모가 작은 것을 먼저 클리어하는 것이 유리
    # 따라서 최소 필요 피로도는 높으면서 소모 피로도는 낮은 순으로 정렬을 해보자.

    # 최소 필요 피로도가 높던 낮던 소모 피로도가 제일 낮은 게 유리할 수도 있다.
    # 케이스를 2개 가져가야 할 것 같다. 소모 피로도가 무조건 낮은 순서로 뽑는 경우와
        # 허나 피로도가 쓸데없이 남을 수 있는 위험이 있다.
    # 무조건 최소 필요 피로도가 높은 순 + 소모 피로도가 낮은 순으로 찾는 경우
        # 허나 피로도를 효율적으로 못 쓸 수 있다.

    # 따라서 이건 깊이 우선 탐색 or BFS로 탐색해야 할 것 같다.
    # k, 던전갯수가 작으므로 완전탐색도 가능 (8! = 약 4만)
    # 미리 8!의 모든 경우의 수를 모듈로 뽑고 풀거나
    # DFS로 모든 경우의 수 탐색을 직접 구현한다. O

    dungeonSize = len(dungeons)
    visitedDungeon = [0 for x in range(dungeonSize)]

    def DFS(depth, hp):
        global answer

        if depth == dungeonSize:
            answer = depth
            return

        for i in range(dungeonSize):
            if visitedDungeon[i] == 0 and hp >= dungeons[i][0]:
                visitedDungeon[i] = 1
                DFS(depth + 1, hp - dungeons[i][1])
                visitedDungeon[i] = 0

        answer = max(answer, depth)

    answer = 0
    DFS(0, k)

    return answer

print(solution(k, dungeons))
