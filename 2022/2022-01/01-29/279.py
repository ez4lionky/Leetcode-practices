from collections import deque


# better pruning, start from target to zero
class Solution:
    def numSquares(self, n: int) -> int:
        deq=deque()
        visited=set()
        # consider residual as node
        # if visited then means that this path is not the shortest
    
        deq.append(n)
        k = 1
        while deq:
            size = len(deq)
            for _ in range(size):
                number=deq.popleft()
                targets=[number-i*i for i in range(1,int(number**0.5)+1)]
                for target in targets:
                    if target==0:return k
                    if target not in visited:
                        deq.append((target))
                        visited.add(target)
            k += 1
        return 0


# pruning but still TLE
# class Solution:
#     def numSquares(self, n: int) -> int:
#         deq=deque()
#         p_nums=list(range(1,int(n**0.5)+1))[::-1]
#         deq.append((0, []))
#         while deq:
#             size = len(deq)
#             for _ in range(size):
#                 s, nums=deq.popleft()
#                 if s == n:
#                     return len(nums)
#                 if s > n:
#                     continue
#                 if len(nums) != 0:
#                     p_nums=list(range(1,int(nums[-1]**0.5)+1))[::-1]
#                 for i in p_nums:
#                     deq.append((s+i**2, nums+[i**2]))
#         return 0



if __name__ == "__main__":
    sol = Solution()
    # print(sol.numSquares(12))
    # print(sol.numSquares(13))
    # print(sol.numSquares(7168))
    print(sol.numSquares(6616))

