from typing import *


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i, n = -1, 0
        while n < l:
            i += 1
            n += 1 if arr[i] else 2
        if n == l + 1:
            n -= 2
            arr[n] = 0
            i -= 1
        while n > 0:
            arr[n-1] = arr[i]
            n -= 1
            if arr[i] == 0:
                arr[n-1] = arr[i]
                n -= 1
            i -= 1
        return
 

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         l = len(arr)
#         flag = False
#         n = 0
#         for i in range(l):
#             if arr[i] == 0:
#                 if n == l-1: n += 1; flag = True
#                 else: n += 2
#             else:
#                 n += 1
#             if n == l:
#                 break
#         while n > 0:
#             if arr[i] == 0:
#                 if n < 2 or (n == l and flag):
#                     arr[n-1] = 0
#                     n -= 1
#                 else:
#                     arr[n-2] = arr[n-1] = 0
#                     n -= 2
#             else:
#                 arr[n-1] = arr[i]
#                 n -= 1
#             i -= 1
#         return


if __name__ == "__main__":
    sol = Solution()
    # arr = [0,0,0,0,0,0,0]
    # arr = [8,4,5,0,0,0,0,7]
    arr = [1,0,2,3,0,4,5,0]
    print(sol.duplicateZeros(arr))

