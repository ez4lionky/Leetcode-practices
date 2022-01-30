from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        items1, items2 = s1.split(), s2.split()
        nums = defaultdict(int)
        for item in items1:
            nums[item] += 1
        for item in items2:
            nums[item] += 1

        res = []
        for k in nums.keys():
            if nums[k] == 1:
                res.append(k)
        return res

        # items1, items2 = s1.split(), s2.split()
        # s1_num, s2_num = defaultdict(int), defaultdict(int)
        # for item in items1:
        #     s1_num[item] += 1
        # for item in items2:
        #     s2_num[item] += 1
        
        # dup_s1_set, dup_s2_set = [], []
        # for k in s1_num.keys():
        #     if s1_num[k] > 1:
        #         dup_s1_set.append(k)
        # for k in s2_num.keys():
        #     if s2_num[k] > 1:
        #         dup_s2_set.append(k)
        # dup_s1_set, dup_s2_set = set(dup_s1_set), set(dup_s2_set)
        # s1_set, s2_set = set(s1_num.keys()), set(s2_num.keys())
        # return list(s1_set - s2_set - dup_s1_set) + list(s2_set - s1_set - dup_s2_set)


if __name__ == "__main__":
    sol = Solution()
    # s1, s2 = "this apple is sweet", "this apple is sour"
    # s1, s2 = "apple apple", "banana"
    s1, s2 = "s z z z s", "s z ejt"
    print(sol.uncommonFromSentences(s1, s2))

