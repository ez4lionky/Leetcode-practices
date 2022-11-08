class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            cur_flag = True
            for w in word:
                if w not in allowed:
                    cur_flag = False
                    break
            if cur_flag:
                res += 1
        return res

