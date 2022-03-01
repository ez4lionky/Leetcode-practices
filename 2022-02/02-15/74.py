from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start <= end:
            mid = (start + end) // 2
            u, v = mid // n, mid % n
            if matrix[u][v] < target:
                start = mid + 1
            elif matrix[u][v] > target:
                end = mid - 1
            else:
                return True
        return False
    

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3
    target = 13
    print(sol.searchMatrix(matrix, target))

