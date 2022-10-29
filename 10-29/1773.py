class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        index = {'type': 0, 'color': 1, 'name': 2}[ruleKey]
        for item in items:
            if item[index] == ruleValue:
                res += 1
        return res

