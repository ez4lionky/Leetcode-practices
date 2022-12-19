class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        n = len(arr)
        return sum(arr[n//20:-n//20]) / (n*0.9)

