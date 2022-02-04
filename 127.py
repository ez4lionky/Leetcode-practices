# from collections import deque


# simplified b-bfs version
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        letters = 'abcdefghijklmnopqrstuvwxyz'
        start_visited, end_visited = {beginWord}, {endWord}
        res = 1

        while start_visited and end_visited:
            if len (start_visited) > len(end_visited):
                start_visited, end_visited = end_visited, start_visited
            next_visited = set()
            for node in start_visited:
                for i in range(len(node)):
                    for l in letters:
                        new_word = node[:i] + l + node[i+1:]
                        if new_word in end_visited:
                            return res + 1
                        if new_word in word_set:
                            # due to greedy property of BFS
                            # we only need to judge if new_word exists in the latest layer.
                            next_visited.add(new_word)
                            word_set.remove(new_word)
            start_visited = next_visited
            res += 1
        return 0


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList):
#         # def diff_letters(a,b):
#         #     return sum ( a[i] != b[i] for i in range(len(a)) )
#
#         def get_neighbours(word, wordList):
#             neighbours = []
#             # word length << length of wordList
#             for i in range(len(word)):
#                 for j in range(97, 123):
#                     n = word[:i] + chr(j) + word[i+1:]
#                     if n in wordList:
#                         neighbours.append(n)
#             # for w in wordList:
#             #     if diff_letters(word, w) == 1:
#             #         neighbours.append(w)
#             return neighbours
#
#         word_set = set(wordList)
#         if endWord not in wordList:
#             return 0
#         start_queue, end_queue = deque(), deque()
#         start_queue.append(beginWord), end_queue.append(endWord)
#         start_visited, end_visited = set(), set()
#         start_visited.add(beginWord), end_visited.add(endWord)
#         res = 1
#         while start_queue and end_queue:
#             if len(start_queue) <= len(end_queue):
#                 cur_queue, cur_visited, next_visited = start_queue, start_visited, end_visited
#             else:
#                 cur_queue, cur_visited, next_visited = end_queue, end_visited, start_visited
#             size = len(cur_queue)
#             for _ in range(size):
#                 node = cur_queue.popleft()
#                 if node in next_visited:
#                     return res
#                 for n in get_neighbours(node, word_set):
#                     if n not in cur_visited:
#                         cur_queue.append(n)
#                         cur_visited.add(n)
#             res += 1
#         return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    # wordList = ["hot","dot","dog","lot","log"]
    print(sol.ladderLength(beginWord, endWord, wordList))

