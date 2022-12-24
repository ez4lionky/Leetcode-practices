# class Solution:
#     def largestMerge(self, word1: str, word2: str) -> str:
#         res = ""
#         i, j, l_i, l_j = 0, 0, 0, 0
#         while i + l_i < len(word1) and j + l_j < len(word2):
#             if word1[i+l_i] < word2[j+l_j]:
#                 res += word2[j:j+l_j+1]
#                 j += l_j + 1
#                 l_j, l_i = 0, 0
#             elif word1[i+l_i] > word2[j+l_j]:
#                 res += word1[i:i+l_i+1]
#                 i += l_i + 1
#                 l_i, l_j = 0, 0
#             else:
#                 l_i, l_j = l_i + 1, l_j + 1
#         res += word1[i:] + word2[j:] if word1[i:] > word2[j:] else word2[j:] + word1[i:]
#         return res


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j, n, m = 0, 0, len(word1), len(word2)
        while i < n or j < m:
            if i < n and word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge)


if __name__ == "__main__":
    sol = Solution()
    # word1, word2 = "abcabc", "abdcaba"
    # print(sol.largestMerge(word1, word2))
    word1, word2 = "guguuuuuuuuuuuuuuguguuuuguug", "gguggggggguuggguugggggg"
    print(sol.largestMerge(word1, word2))
    print("guguuuuuuuuuuuuuuguguuuuguugguggggggguuggguuggggggg")
    print(sol.largestMerge(word1, word2) == "guguuuuuuuuuuuuuuguguuuuguugguggggggguuggguuggggggg")

