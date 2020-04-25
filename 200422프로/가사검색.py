words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "???ao", "???"]

# Trie 구조를 만드는 데 참조한 사이트
# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

class Node(object):

    def __init__(self, key, data=None):
        self.key = key
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}


class Trie(object):

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # When we have reached the end of the string, set the curr_node's data to string.
        # This also denotes that curr_node represents the final character of string.
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # Reached the end of string,
        # If curr_node has data (i.e. curr_node is not None), string exists in the trie
        if (curr_node.data != None):
            return True

    def starts_with(self, prefix, l):
        curr_node = self.head
        result = 0
        subtrie = None

        # Locate the prefix in the trie,
        # and make subtrie point to prefix's last character Node
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return 0

        # Using BFS, traverse through the prefix subtrie,
        # and look for nodes with non-null data fields.

        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None and len(curr.data) == l:
                result += 1

            queue += list(curr.children.values())

        return result

def solution(words, queries):
    answer = []
    t = Trie()
    rev_t = Trie()
    re_words = [word[::-1] for word in words]
    nums = {}
    for word in words:
        if len(word) not in nums:
            nums[len(word)] = 1
        else:
            nums[len(word)] += 1
    rec = {}
    for i in range(len(words)):
        t.insert(words[i])
        rev_t.insert(re_words[i])

    for querie in queries:
        if querie in rec:
            answer.append(rec[querie])
            continue
        type = cnt = 0
        if querie[0] == '?' and querie[-1] == '?':
            if len(querie) not in nums:
                answer.append(0)
            else:
                answer.append(nums[len(querie)])
            continue
        elif querie[-1] == '?':
            type = 1
            tmp = querie[:querie.find('?')]
            cnt = t.starts_with(tmp, len(querie))
            answer.append(cnt)
        else:
            tmp = querie[-querie[::-1].find('?'):][::-1]
            cnt = rev_t.starts_with(tmp, len(querie))
            answer.append(cnt)
        rec[querie] = cnt
    return answer

print(solution(words, queries))

###########################################################
# 트라이 구조 알고리즘 적용 없이 선형으로 구현했던 것(효율 4/5)
def solution(words, queries):
    answer = []
    nums = {}
    for word in words:
        if len(word) not in nums:
            nums[len(word)] = 1
        else:
            nums[len(word)] += 1
    rec = {}
    for querie in queries:
        if querie in rec:
            answer.append(rec[querie])
            continue
        type = cnt = 0
        if querie[-1] == '?' and querie[0] == '?':
            if len(querie) not in nums:
                answer.append(0)
            else:
                answer.append(nums[len(querie)])
            continue
        if querie[-1] == '?':
            type = 1
            tmp = querie[:querie.find('?')]
        else:
            tmp = querie[-querie[::-1].find('?'):]

        for word in words:
            if len(word) == len(querie):
                if type and tmp == word[:len(tmp)]:
                    cnt += 1
                elif type == 0 and tmp == word[-len(tmp):]:
                    cnt += 1
        answer.append(cnt)
        rec[querie] = cnt
    return answer

print(solution(words, queries))

################################################################
# 이분탐색으로 풀어보려고 했던 시도

# def solution(words, queries):
#     answer = []
#     re_words = [word[::-1] for word in words]
# #     re_words.sort()
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

# Test
# t = Trie()
# words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
# for word in words:
#     t.insert(word)
#
# print(t.search("romulus"))
# print(t.search("ruler"))
# print(t.search("rulere"))
# print(t.search("romunus"))
# print(t.starts_with("ro"))
# print(t.starts_with("ssda"))
# print(t.starts_with("rube"))