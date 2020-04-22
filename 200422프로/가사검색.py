words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    for querie in queries:
        type = cnt = 0
        if querie[-1] == '?':
            type = 1
            tmp = querie[:querie.find('?')]
        else:
            tmp = querie[-querie[::-1].find('?'):]

        for word in words:
            if len(word) == len(querie):
                if tmp == '':
                    cnt += 1
                elif type and tmp == word[:len(tmp)]:
                    cnt += 1
                elif type == 0 and tmp == word[-len(tmp):]:
                    cnt += 1
        answer.append(cnt)
    return answer

# def solution(words, queries):
#     answer = []
#     re_words = [word[::-1] for word in words]
#     re_words.sort()
#     print(re_words)
#     words.sort()
#     print(words)
#     for querie in queries:
#         cnt = 0
#         type = 1
#         if querie[-1] == '?':
#             tmp = querie[:querie.find('?')]
#         else:
#             type = 2
#             tmp = querie[-querie[::-1].find('?'):][::-1]
#             print(tmp)
#         if tmp == '':
#             for word in words:
#                 if len(word) == len(querie): cnt += 1
#             answer.append(cnt)
#         else:
#             t = -1
#             l, r = 0, len(words) - 1
#             while l <= r:
#                 mid = (l + r) // 2
#                 if type == 1:
#                     if tmp < words[mid][:len(tmp)]:
#                         r = mid - 1
#                     elif tmp > words[mid][:len(tmp)]:
#                         l = mid + 1
#                     else:
#                         t = mid
#                         break
#
#                 else:
#                     if tmp < re_words[mid][:len(tmp)]:
#                         r = mid - 1
#                     elif tmp > re_words[mid][:len(tmp)]:
#                         l = mid + 1
#                     else:
#                         t = mid
#                         break
#             print(t)
#             if t < 0:
#                 answer.append(0)
#             else:
#                 cnt += 1
#                 if type == 1:
#                     for i in range(t + 1, len(words)):
#                         if len(querie) != len(words[i]) or tmp != words[i][:len(tmp)]: break
#                         cnt += 1
#                     for i in range(t - 1, -1, -1):
#                         if len(querie) != len(words[i]) or tmp != words[i][:len(tmp)]: break
#                         cnt += 1
#                 else:
#                     for i in range(t + 1, len(words)):
#                         if len(querie) != len(words[i]) or tmp != re_words[i][:len(tmp)]: break
#                         cnt += 1
#                     for i in range(t - 1, -1, -1):
#                         if len(querie) != len(words[i]) or tmp != re_words[i][:len(tmp)]: break
#                         cnt += 1
#                 answer.append(cnt)
#     return answer

print(solution(words, queries))