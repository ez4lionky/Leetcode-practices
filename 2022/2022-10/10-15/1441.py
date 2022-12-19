# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         stack, res = [], []
#         for i in range(1, n+1):
#             if i in target:
#                 res.append('Push')
#                 stack.append(i)
#             else:
#                 res.append('Push')
#                 res.append('Pop')
#             if stack == target:
#                 break
#         return res


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pre, res = 0, []
        for i in range(1, n+1):
            if i in target:
                res.append('Push')
                pre = i
            else:
                res.append('Push')
                res.append('Pop')
            if pre == target[-1]:
                break
        return res

