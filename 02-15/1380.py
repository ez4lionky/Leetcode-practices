from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_mins = set()
        for row in matrix:
            row_mins.add(min(row))
        for i in range(len(matrix[0])):
            cur_max = max([row[i] for row in matrix])
            if cur_max in row_mins:
                res.append(cur_max)
                break
        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(sol.luckyNumbers(matrix))

