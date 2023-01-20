from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(set)
        for uid, mid in logs:
            counter[uid].add(mid)
        res = [0 for _ in range(k)]
        for k, v in counter.items():
            if 0 < len(v):
                res[len(v)-1] += 1
        return res


