from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def int2bin(n, count=12):
            """returns the binary of integer n, using count number of digits"""
            return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

        bobArrorws = [0 for _ in range(12)]
        best_score = -1
        for i in range(2**12):
            s = int2bin(i)
            num, score, cur = 0, 0, [0 for _ in range(12)]
            for j in range(12):
                if s[j] == '1':
                    c = aliceArrows[j] + 1
                    num += c
                    score += j
                    cur[j] = c
            if num <= numArrows and score > best_score:
                best_score = score
                if numArrows > num:
                    cur[0] += numArrows - num
                bobArrorws = cur
        return bobArrorws


if __name__ == "__main__":
    sol = Solution()
    numArrows = 9
    aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
    numArrows = 89
    aliceArrows = [3,2,28,1,7,1,16,7,3,13,3,5]
    print(sol.maximumBobPoints(numArrows, aliceArrows))

