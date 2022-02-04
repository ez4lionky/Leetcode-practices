from collections import deque, defaultdict


class Solution:
    # vanilla version: Breadth First Search
    # def openLock(self, deadends, target: str) -> int:
    #     if "0000" in deadends:
    #         return -1
    #     visited = defaultdict(bool)
    #     for d in deadends:
    #         visited[d] = True
    #     queue = deque(['0000'])
    #     visited['0000'] = True
    #     k = 0
    #     while queue:
    #         size = len(queue)
    #         for _ in range(size):
    #             vid = queue.popleft()
    #             if vid == target:
    #                 return k
    #             for i, s in enumerate(vid):
    #                 s = int(s)
    #                 pre_v = vid[:i] + str((s - 1) % 10) + vid[i+1:]
    #                 next_v = vid[:i] + str((s + 1) % 10) + vid[i+1:]
    #                 if not visited[pre_v]:
    #                     queue.append(pre_v)
    #                     visited[pre_v] = True
    #                 if not visited[next_v]:
    #                     queue.append(next_v)
    #                     visited[next_v] = True
    #         k += 1
    #     return -1


    # optimized version: Bidirectional BFS
    # def openLock(self, deadends, target):
    #     def get_neighbours(string):
    #         neighbours = []
    #         for i,c in enumerate(string):
    #             neighbours.append(string[:i] + str((int(c) + 1) % 10) + string[i+1:])
    #             neighbours.append(string[:i] + str((int(c) - 1) % 10) + string[i+1:])
    #         return neighbours
    #
    #     if "0000" in deadends:
    #         return -1
    #     if target == "0000":
    #         return 0
    #
    #     k = 0
    #     start_queue, end_queue = deque(), deque()
    #     start_queue.append("0000"), end_queue.append(target)
    #     start_visited, end_visited = set(), set()
    #     start_visited.add("0000"), end_visited.add(target)
    #     while start_queue and end_queue:
    #         start_size, end_size = len(start_queue), len(end_queue)
    #         k += 1
    #         for _ in range(start_size):
    #             vid = start_queue.popleft()
    #             neighbours = get_neighbours(vid)
    #             for n in neighbours:
    #                 if n not in start_visited and n not in deadends:
    #                     if n in end_visited:
    #                         return k
    #                     start_queue.append(n)
    #                     start_visited.add(n)
    #
    #         k += 1
    #         for _ in range(end_size):
    #             vid = end_queue.popleft()
    #             neighbours = get_neighbours(vid)
    #             for n in neighbours:
    #                 if n not in end_visited and n not in deadends:
    #                     if n in start_visited:
    #                         return k
    #                     end_queue.append(n)
    #                     end_visited.add(n)
    #
    #     return -1
    
    # Bidirectional BFS with automatic balancing
    def openLock(self, deadends, target):
        def get_neighbours(string):
            neighbours = []
            for i,c in enumerate(string):
                neighbours.append(string[:i] + str((int(c) + 1) % 10) + string[i+1:])
                neighbours.append(string[:i] + str((int(c) - 1) % 10) + string[i+1:])
            return neighbours

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        k = 1
        start_queue, end_queue = deque(), deque()
        start_queue.append("0000"), end_queue.append(target)
        start_visited, end_visited = set(), set()
        start_visited.add("0000"), end_visited.add(target)
        # directed graph use or, undirected graph use and
        while start_queue and end_queue:
            if len(start_queue) > len(end_queue):
                cur_queue, cur_visited, next_queue, next_visited = end_queue, end_visited, start_queue, start_visited
            else:
                cur_queue, cur_visited, next_queue, next_visited = start_queue, start_visited, end_queue, end_visited

            size = len(cur_queue)
            for _ in range(size):
                vid = cur_queue.popleft()
                neighbours = get_neighbours(vid)
                for n in neighbours:
                    if n not in cur_visited and n not in deadends:
                        if n in next_visited:
                            return k
                        cur_queue.append(n)
                        cur_visited.add(n)
            k += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    # deadends = ["8887", "8889","8878","8898","8788","8988","7888","9888"]
    # target = "8888"
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    # deadends = ["0000"]
    # target = "8888"
    print(sol.openLock(deadends, target))

