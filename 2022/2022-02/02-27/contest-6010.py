from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # res < max_time
        time = sorted(time)
        max_time = totalTrips * time[0]
        start, end = time[0], max_time
        while start <= end:
            mid = (start + end) // 2
            step = 0
            for t in time:
                if t > mid:
                    break
                step += mid // t
            if step < totalTrips:
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == "__main__":
    sol = Solution()
    # time = [1,2,3]
    # totalTrips = 5
    time = [2]
    totalTrips = 1
    print(sol.minimumTime(time, totalTrips))

