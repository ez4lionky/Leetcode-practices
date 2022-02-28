from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        delta = [0 for _ in range(n)]
        ans, cnt, z_num = 0, 0, n
        def backtracking(pos):
            nonlocal ans, cnt, z_num
            if pos == len(requests):
                if z_num == n:
                    ans = max(ans, cnt)
                return

            for i in range(pos, len(requests)):
                f, t = requests[i]
                pre = sum([delta[f]==0, delta[t]==0])
                delta[f] = delta[f] - 1
                delta[t] = delta[t] + 1
                cur = sum([delta[f]==0, delta[t]==0])
                z_num += (cur - pre)
                cnt += 1
                backtracking(i+1)
                cnt -= 1
                z_num -= (cur - pre)
                delta[f] = delta[f] + 1
                delta[t] = delta[t] - 1
            if z_num == n:
                ans = max(ans, cnt)
            return
        backtracking(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    # n = 5
    # requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    # n = 3
    # requests = [[0,0],[1,2],[2,1]]
    # n = 3
    # requests = [[2,0],[0,0],[1,2],[0,0]]
    # requests = [[0,0],[0,0]]
    n = 1
    requests = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    print(sol.maximumRequests(n, requests))

