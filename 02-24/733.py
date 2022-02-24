from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        m, n = len(image), len(image[0])
        visited = set([(sr, sc)])
        queue = deque([(sr, sc)])
        ori_c = image[sr][sc]
        offsets = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while queue:
            r, c = queue.pop()
            for x, y in offsets:
                if 0<=r+x<m and 0<=c+y<n and (r+x, c+y) not in visited and image[r+x][c+y]==ori_c:
                    queue.append((r+x, c+y))
                    visited.add((r+x, c+y))
        for r, c in visited:
            image[r][c] = newColor
        return image


if __name__ == "__main__":
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(sol.floodFill(image, sr, sc, newColor))

