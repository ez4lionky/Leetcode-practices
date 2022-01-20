# My primary solution is:
# while k:
#   find the smallest number in k+1 numbers
#   delete others before the smallest number
#   k - delete_num
# Here is the implementation of using stack

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        s = []
        while k and i < len(num):
            if len(s) and s[-1] > num[i]:
                s.pop(-1)
                k -= 1
            else:
                s.append(num[i])
                i += 1
        if k:
            while k:
                s.pop(-1)
                k -= 1
        if i == len(num):
            result = ''.join(s)
        else:
            result = ''.join(s) + num[i:]
        while len(result) > 1 and result[0] == '0':
            result = result[1:]
        if result == '':
            return '0'
        return result


sol = Solution()
num = "1432219"
k = 3
print(sol.removeKdigits(num, k))
num = "10200"
k = 1
print(sol.removeKdigits(num, k))
num = "10"
k = 2
print(sol.removeKdigits(num, k))
