from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []
        for idx, n in enumerate(nums):
            n = list(str(n))
            str_n = ''
            for i in range(len(n)):
                str_n += str(mapping[int(n[i])])
            mapped_nums.append((int(str_n), idx))
        mapped_nums = sorted(mapped_nums)
        return [nums[i[1]] for i in mapped_nums]


if __name__ == "__main__":
    sol = Solution()
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]
    print(sol.sortJumbled(mapping, nums))

