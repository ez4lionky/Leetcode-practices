from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # cnt = Counter(ch for ch in text if ch in "balon")
        cnt = Counter(list(filter(lambda ch: ch in 'balon', text)))
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values()) if len(cnt) == 5 else 0


# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         nums = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
#         for ch in text:
#             if ch in ['b', 'a', 'n']:
#                 nums[ch] += 2
#             elif ch in ['l', 'o']:
#                 nums[ch] += 1
#         return min(nums.values()) // 2


if __name__ == "__main__":
    # text = "nlaebolko"
    text = "loonbalxballpoon"
    # text = "lloo"
    sol = Solution()
    print(sol.maxNumberOfBalloons(text))

