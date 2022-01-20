import copy


class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        results = []
        location = [['.' for _ in range(n)] for _ in range(n)]
        mark = [[0 for _ in range(n)] for _ in range(n)]
        self.generate(0, n, location, mark, results)
        for i in range(len(results)):
            for j in range(n):
                s = ''.join(results[i][j])
                results[i][j] = s
        return results

    def put_down_the_queen(self, x, y, mark):
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        mark[x][y] = 1
        size = len(mark) - min([x, y])
        for i in range(1, size):
            for j in range(len(dx)):
                new_x = x + dx[j] * i
                new_y = y + dy[j] * i
                if 0 <= new_x < len(mark) and 0 <= new_y < len(mark):
                    mark[new_x][new_y] = 1

    def generate(self, k, n, location, mark, results):
        if k == n:
            results.append(copy.deepcopy(location))
            return
        for i in range(n):
            if mark[k][i] == 0:
                tmp_mark = copy.deepcopy(mark)
                location[k][i] = 'Q'
                self.put_down_the_queen(k, i, mark)
                self.generate(k + 1, n, location, mark, results)
                mark = tmp_mark
                location[k][i] = '.'


sol = Solution()
n = 4
print(sol.solveNQueens(n))
