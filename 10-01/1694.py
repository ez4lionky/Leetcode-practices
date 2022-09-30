class Solution:
    def reformatNumber(self, number: str) -> str:
        number = "".join([ch for ch in number if ch not in [" ", "-"]])
        l = len(number)
        if l < 4:
            return number
        n, r = divmod(l, 3)
        res = ""
        i = 0
        while i < n - 1:
            res += number[i*3:(i+1)*3] + "-"
            i += 1
        if r == 1:
            res += number[i*3:i*3+2] + '-' + number[i*3+2:]
        elif r == 2:
            res += number[i*3:(i+1)*3] + '-' + number[-2:]
        else:
            res += number[i*3:]
        return res

