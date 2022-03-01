class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


# O(n) = n! 
# class Solution:
#     def dailyTemperatures(self, temperatures):
#         temperatures = deque(temperatures)
#         res = []
#         while temperatures:
#             t = temperatures.popleft()
#             if_larger = False
#             for i, v in enumerate(temperatures):
#                 if v > t:
#                     res.append(i + 1)
#                     if_larger = True
#                     break
#             if not if_larger:
#                 res.append(0)
#         return res


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))

