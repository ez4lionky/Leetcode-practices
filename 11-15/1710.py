class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        res, num = 0, 0
        for b in boxTypes:
            if num + b[0] <= truckSize:
                res += b[0] * b[1]
                num += b[0]
            else:
                left = truckSize - num
                res += left * b[1]
                break
        return res

