class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        def diff_letters(a,b):
            return sum ( a[i] != b[i] for i in range(len(a)) )

        def get_neighbours(node, bank_set):
            neighbours = []
            for g in bank_set:
                if diff_letters(node, g) == 1:
                    neighbours.append(g)
            return neighbours

        visited = {start}
        bank = set(bank)
        res = 0
        while visited:
            next_visited = set()
            for node in visited:
                if node == end:
                    return res
                for g in get_neighbours(node, bank):
                    next_visited.add(g)
                    bank.remove(g)
            visited = next_visited
            res += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    # start = "AACCGGTT"
    # end = "AACCGGTA"
    # bank = ["AACCGGTA"]
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(sol.minMutation(start, end, bank))

