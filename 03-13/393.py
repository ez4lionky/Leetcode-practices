from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def valid(n):
            return 128<=n<=191

        n = len(data)
        res = True
        i = 0
        while i<len(data):
            d = data[i]
            if d <= 127:
                i += 1
                continue
            elif 192 <= d <= 223:
                if i+1<n and valid(data[i+1]):
                    i += 2
                    continue
            elif 224 <= d <= 239:
                if (i+2)<n and valid(data[i+1]) and valid(data[i+2]):
                    i += 3
                    continue
            elif 240 <= d <= 247:
                if (i+3)<n and valid(data[i+1]) and valid(data[i+2]) and valid(data[i+3]):
                    i += 4
                    continue
            res = False
            break
        return res


if __name__ == "__main__":
    sol = Solution()
    # data = [197,130,1]
    # data = [235,140,4]
    data = [237]
    print(sol.validUtf8(data))

