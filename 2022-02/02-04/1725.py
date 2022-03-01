class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        max_len, res = 0, 0
        for l, w in rectangles:
            max_l = min(l, w)
            if max_len < max_l:
                max_len = max_l
                res = 1
            elif max_len == max_l:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # rectangles = [[5,8],[3,9],[5,12],[16,5]]
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    print(sol.countGoodRectangles(rectangles))

