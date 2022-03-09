from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffs = [0] * n
        for x, y, num in bookings:
            diffs[x-1] += num
            if y != n:
                diffs[y] -= num
        res, pre_s = [], 0
        for d in diffs:
            pre_s += d
            res.append(pre_s)
        return res


if __name__ == "__main__":
    sol = Solution()
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print(sol.corpFlightBookings(bookings, n))

