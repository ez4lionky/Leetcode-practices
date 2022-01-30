from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        deq=deque()
        visited=set()
       
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


if __name__ == "__main__":
    sol = Solution()
    # print(sol.numSquares(12))
    print(sol.numSquares(7168))

