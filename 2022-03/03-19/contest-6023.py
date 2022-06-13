# import heapq
#
#
# class Solution:
#     def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
#         w_s = 0
#         n = len(floor)
#         pre_sum = [0] * (n+1)
#         for i, f in enumerate(floor):
#             if f == '1':
#                 w_s += 1
#             pre_sum[i+1] = w_s
#         diffs = []
#         for i in range(n-carpetLen+1):
#             l, r = i, i + carpetLen
#             diffs.append(pre_sum[r] - pre_sum[l])
#         for _ in range(numCarpets):
#             max_d = max(diffs)
#             diffs[i] = 0
#             for a, b in r
#         # print(pre_sum)
#         # print(diffs)
#         # print(heapq.nlargest(numCarpets, diffs))
#         # print(sum(heapq.nlargest(numCarpets, diffs)))
#         return max(w_s - sum(heapq.nlargest(numCarpets, diffs)), 0)
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     # floor = "10110101"
#     # numCarpets = 2
#     # carpetLen = 2
#     floor = "1000000000001000000100111100001101111000000001001111110000000000"
#     numCarpets = 6
#     carpetLen = 4
#     print(sol.minimumWhiteTiles(floor, numCarpets, carpetLen))

