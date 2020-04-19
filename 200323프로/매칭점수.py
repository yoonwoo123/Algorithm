import sys, re
# sys.stdin = open("매칭점수_input.txt")

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

answer = 0 # 점수가 가장큰 페이지 idx
word = word.lower()
# (사이트명, 기본점수) 를 배열로 정리해두자.
scores = []
for page in pages:
    tmp = ['', [], 0]
    for sp in page.split(' '):
        # print(sp)
        if sp[0:8] == 'content=':
            a = sp.split('"')
            tmp[0] = a[1]
        elif sp[0:5] == 'href=':
            a = sp.split('"')
            tmp[1].append(a[1])
        for c in re.findall('[a-zA-Z]+', sp):
            # print(c.lower(), word)
            if c.lower() == word:
                # print('good', c)
                tmp[2] += 1

    scores.append(tmp)
L = len(scores)
max_score = 0 # 가장 큰 점수
for i in range(L):
    score = scores[i][2]
    for j in range(L):
        if i == j: continue
        if scores[i][0] in scores[j][1]:
            score += scores[j][2] / len(scores[j][1])
        if max_score < score:
            max_score = score
            answer = i

# print(scores)
# print(answer)

##############################################################################
# 아래는 고수의 풀이법.. 이런식으로 푸는 법을 익히자
def getScore(word, page):
    return re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())

def solution(word, pages):
    webpages = {}
    for i, page in enumerate(pages):
        # print(page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0])
        pagetitle = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        links = []
        # print(page.split('a href=\"')[1:])
        for link_long in page.split('a href=\"')[1:]:
            # print(link_long.split('\"')[0])
            links.append(link_long.split('\"')[0])
        webpages[pagetitle] = [i, getScore(word, page), links, 0] #3은 링크점수

    for page in webpages.values():
        for target in page[2]:
            try:
                webpages[target][3] += page[1] / len(page[2])
            except:
                pass
    answer = []
    # print(webpages)
    for page in webpages.values():
        answer.append([page[0], page[1] + page[3]])

    answer.sort(key=lambda x:x[0])
    return sorted(answer, key=lambda x:x[1], reverse=True)[0][0]
print(solution(word, pages))