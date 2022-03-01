from typing import List
from collections import Counter


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = set()
        rows, cols, diagonal, reverse_diagonal = Counter(), Counter(), Counter(), Counter()
        for i, j in lamps:
            if (i,j) not in points:
                points.add((i, j))
                rows[i] += 1
                cols[j] += 1
                diagonal[i-j] += 1
                reverse_diagonal[i+j] += 1
        print(rows, cols, diagonal, reverse_diagonal)
        ans = []
        for i, j in queries:
            if rows[i] > 0 or cols[j] > 0 or diagonal[i-j] > 0 or reverse_diagonal[i+j] > 0:
                ans.append(1)
            else:
                ans.append(0)
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if n>i+x>=0 and n>j+y>=0 and (i+x, j+y) in points:
                        points.remove((i+x, j+y))
                        rows[i+x] -= 1
                        cols[j+y] -= 1
                        diagonal[i+x-j-y] -= 1
                        reverse_diagonal[i+x+j+y] -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 5
    # lamps = [[0,0],[4,4]]
    # queries = [[1,1],[1,1]]
    # lamps = [[0,0],[4,4]]
    # queries = [[1,1],[1,0]]
    # lamps = [[0,0],[0,4]]
    # queries = [[0,4],[0,1],[1,4]]
    lamps = [[0,0],[1,0]]
    queries = [[1,1],[1,1]]  # out should be (1, 0)
    print(sol.gridIllumination(n, lamps, queries))

