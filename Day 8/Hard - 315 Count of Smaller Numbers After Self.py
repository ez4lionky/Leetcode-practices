# 函数传参传的是对象，参数的传递本质上是一种赋值操作，而赋值是一种名字到对象的绑定操作
# The parameter passed in function call is the object, the parameter passing is essentially an assignment operation,
# and the assignment is a variable-name-to-object operation.


class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        counts = []
        pairs = []
        for j, i in enumerate(nums):
            pairs.append([i, j])
            counts.append(0)
        self.merge_sort(pairs, counts)
        return counts

    def merge_sort(self, pairs, counts):
        if len(pairs) < 2:
            return pairs
        mid = len(pairs) // 2
        sub_pairs1 = []
        sub_pairs2 = []
        for i in range(mid):
            sub_pairs1.append(pairs[i])
        for i in range(mid, len(pairs)):
            sub_pairs2.append(pairs[i])
        sub_pairs1 = self.merge_sort(sub_pairs1, counts)
        sub_pairs2 = self.merge_sort(sub_pairs2, counts)
        return self.merge_sort_two_pairs(sub_pairs1, sub_pairs2, counts)

    def merge_sort_two_pairs(self, pairs1, pairs2, counts):
        i = 0
        j = 0
        result = []
        while i < len(pairs1) and j < len(pairs2):
            if pairs1[i][0] <= pairs2[j][0]:
                result.append(pairs1[i])
                counts[pairs1[i][1]] += j
                i += 1
            else:
                result.append(pairs2[j])
                j += 1
        for ii in range(i, len(pairs1)):
            counts[pairs1[ii][1]] += j
            result.append(pairs1[ii])
        if j < len(pairs2):
            result.extend(pairs2[j:])
        return result


sol = Solution()
# nums = [5, 2, 6, 1]
# print(sol.countSmaller(nums))
nums = [-1, -1]
print(sol.countSmaller(nums))
