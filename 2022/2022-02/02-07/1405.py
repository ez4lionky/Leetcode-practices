import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0: heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: heapq.heappush(max_heap, (-b, 'b'))
        if c > 0: heapq.heappush(max_heap, (-c, 'c'))

        res = ''
        while max_heap:
            n, x = heapq.heappop(max_heap)
            n *= -1
            if len(res) < 2 or not (res[-2] == res[-1] == x):
                res += x
                n -= 1
                if n != 0:
                    heapq.heappush(max_heap, (-n, x))
            else:
                if len(max_heap) == 0:
                    break
                n2, y = heapq.heappop(max_heap)
                n2 *= -1
                res += y
                n2 -= 1
                if n2 != 0:
                    heapq.heappush(max_heap, (-n2, y))
                heapq.heappush(max_heap, (-n, x))
        return res


if __name__ == "__main__":
    sol = Solution()
    a = 1
    b = 1
    c = 7
    print(sol.longestDiverseString(a, b, c))

