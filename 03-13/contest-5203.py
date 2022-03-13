from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(n)]
        for d in dig:
            mat[d[0]][d[1]] = 1
        dp=[[0 for _ in range(n)]for _ in range(n)]
        dp[0][0]=mat[0][0]
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+mat[0][i]
        for j in range(1,n):
            dp[j][0]=dp[j-1][0]+mat[j][0]
            
        #利用递推公式完善dp数组
        for i in range(1,n):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]+mat[i][j]-dp[i-1][j-1]
        res = 0
        for r1, c1, r2, c2 in artifacts:
            s = dp[r2][c2]
            if r1!=0 and c1!=0:
                s = s - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
            elif r1==0 and c1==0:
                pass
            elif r1!=0:
                s = s - dp[r1-1][c2]
            else:
                s = s - dp[r2][c1-1]
            if s >= (r2-r1+1)*(c2-c1+1):
                res += 1
        return res
        

if __name__ == "__main__":
    sol = Solution()
    n = 2
    # artifacts = [[0,0,0,0],[0,1,1,1]]
    # dig = [[0,0],[0,1]]
    artifacts = [[0,0,0,0],[0,1,1,1]]
    dig = [[0,0],[0,1],[1,1]]
    print(sol.digArtifacts(n, artifacts, dig))

