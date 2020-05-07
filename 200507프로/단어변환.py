begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log']

def solution(begin, target, words):
    global answer
    answer = 99999
    visited = [0 for _ in range(len(words))]
    if target not in words:
        return 0

    def check(begin, word):
        cnt = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                # if word[i] != target[i]: return False
                cnt += 1
                if cnt > 1: return False
        if cnt == 0: return False
        return True


    def DFS(dep, begin):
        global answer
        if begin == target:
            answer = min(answer, dep)
            return

        for i in range(len(words)):
            if check(begin, words[i]) and visited[i] == 0:
                visited[i] = 1
                DFS(dep + 1, words[i])
                visited[i] = 0

    DFS(0, begin)
    if answer == 99999:
        return 0
    return answer

print(solution(begin, target, words))