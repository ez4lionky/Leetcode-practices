# shouldn't be i+1, actually, i and i+n also can count 1
# class Solution:
#     def winnerOfGame(self, colors: str) -> bool:
#         l = len(colors)
#         i = 1
#         num_A, num_B = 0, 0
#         while i < l-1:
#             if colors[i] == 'A' and colors[i+1] == 'A' and i+1 != l-1:
#                 num_A += 1
#                 i+=2
#             elif colors[i] == 'B' and colors[i+1] == 'B' and i+1 != l-1:
#                 num_B += 1
#                 i+=2
#             else: i+=1
#         if num_A <= num_B or num_A == 0:
#             return False
#         return True


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = 'C', 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[ord(cur) - ord('A')] += 1
        return freq[0] > freq[1]


if __name__ == "__main__":
    sol = Solution()
    # colors = "BBAA"
    colors = "AAAABBBB"
    print(sol.winnerOfGame(colors))

