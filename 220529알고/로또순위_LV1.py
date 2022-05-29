import sys

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):

    # 우선 lottos와 win_nums 에서 일치하는 갯수를 세주자.
        # 7 - 일치하는 갯수 < 6 이면 그것이 최저등수
        # 7 - 일치하는 갯수 >= 6 이면 최저등수 6 고정

    # set()에 담아서 교집합으로 찾던가 이중 for문으로 일일히 비교(NxM)
    # set() 을 이용한 교집합은 N + M 이므로 시간복잡도 훨씬 줄어들게 변경

    # 최고등수는 7 - (일치하는 갯수 + 0의 갯수)  < 6이면 최고등수
    # 7 - (일치하는 갯수 + 0 의 갯수 ) >= 6이면 최고등수 6 고정

    rank = 7
    zeroCnt = 0
    setLottos = set(lottos)
    setWinNums = set(win_nums)
    correctCnt = len(setLottos & setWinNums)

    for num in lottos:
        if num == 0:
            zeroCnt += 1

    bestRank = 7 - (correctCnt + zeroCnt)
    worstRank = 7 - (correctCnt)

    if bestRank >= 6:
        bestRank = 6

    if worstRank >= 6:
        worstRank = 6

    return [bestRank, worstRank]

print(solution(lottos, win_nums))


