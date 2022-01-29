# vanilla version: Breadth First Search
from collections import deque, defaultdict


class Solution:
    def openLock(self, deadends, target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = defaultdict(bool)
        for d in deadends:
            visited[d] = True
        queue = deque(['0000'])
        visited['0000'] = True
        k = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                vid = queue.popleft()
                if vid == target:
                    return k
                for i, s in enumerate(vid):
                    s = int(s)
                    pre_v = vid[:i] + str((s - 1) % 10) + vid[i+1:]
                    next_v = vid[:i] + str((s + 1) % 10) + vid[i+1:]
                    if not visited[pre_v]:
                        queue.append(pre_v)
                        visited[pre_v] = True
                    if not visited[next_v]:
                        queue.append(next_v)
                        visited[next_v] = True
            k += 1
        return -1


# optimized version: Bidirectional BFS


if __name__ == "__main__":
    sol = Solution()
    # deadends = ["8887", "8889","8878","8898","8788","8988","7888","9888"]
    # target = "8888"
    # deadends = ["0201","0101","0102","1212","2002"]
    # target = "0202"
    deadends = ["0000"]
    target = "8888"
    print(sol.openLock(deadends, target))

