from sys import float_info
from typing import List


# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         s = float('inf')
#         res = []
#         for i, r1 in enumerate(list1):
#             for j, r2 in enumerate(list2):
#                 if i + j > s:
#                     break
#                 if r1 == r2:
#                     if s == i+j:
#                         res.append(r1)
#                     else:
#                         res = [r1]
#                         s = i + j
#         return res


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            return self.findRestaurant(list2, list1)
        l1 = {l:i for i, l in enumerate(list1)}
        s, res = float('inf'), []
        for i, l in enumerate(list2):
            if l in l1.keys():
                cur = i + l1[l]
                if cur > s:
                    continue
                elif cur == s:
                    res.append(l)
                else:
                    res = [l]
                    s = cur
        return res


if __name__ == "__main__":
    sol = Solution()
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(sol.findRestaurant(list1, list2))

