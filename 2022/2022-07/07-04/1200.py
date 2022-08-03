class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff = 10**9
        pairs = []
        for i in range(len(arr)-1):
            cur_diff = abs(arr[i+1] - arr[i]) 
            if cur_diff < min_diff:
                pairs = [[arr[i], arr[i+1]]]
                min_diff = cur_diff
            elif cur_diff == min_diff:
                pairs.append([arr[i], arr[i+1]])
        return pairs

