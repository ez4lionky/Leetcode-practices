class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        i_sum, num_sum = 0, 0
        for i in range(len(arr)):
            i_sum += i
            num_sum += arr[i]
            if i_sum == num_sum:
                res += 1
            else:
                i_sum, num_sum = i, arr[i]
        return res

