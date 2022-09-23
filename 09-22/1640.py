class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {p[0]: [i, len(p)] for i, p in enumerate(pieces)}
        max_l = len(arr)
        i = 0
        while i < max_l:
            if arr[i] not in index:
                return False
            ind, l = index[arr[i]]
            p = pieces[ind]
            if arr[i:i+l] != p:
                return False
            i += l
        return True

