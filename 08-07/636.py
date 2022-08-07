from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for l in logs:
            idx, action, ts = l.split(":")
            idx, ts = int(idx), int(ts)
            if action[0] == 's':
                if stack:
                    res[stack[-1][0]] += ts - stack[-1][1]
                    stack[-1][1] = ts
                stack.append([idx, ts])
            else:
                top = stack.pop()
                res[top[0]] += ts - top[1] + 1
                if stack:
                    stack[-1][1] = ts + 1
        return res


if __name__ == "__main__":
    sol = Solution()
    
