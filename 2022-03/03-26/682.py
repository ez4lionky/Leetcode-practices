from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op.isdigit() or op[0] == '-':
                res.append(int(op))
            elif op == 'C':
                res.pop()
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == '+':
                res.append(res[-1] + res[-2])
        return sum(res)


if __name__ == "__main__":
    sol = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    print(sol.calPoints(ops))

