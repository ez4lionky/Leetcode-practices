class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = list(range(left, right+1))
        res = []
        for n in nums:
            flag = True
            s = str(n)
            if '0' in s:
                continue
            for c in s:
                if n % int(c) != 0:
                    flag = False
            if flag:
                res.append(n)
        return res

