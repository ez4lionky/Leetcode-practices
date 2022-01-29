class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort()
        res = 0
        a, d = properties.pop()
        a_less = False
        prev_d = d
        while properties:
            _a, _d = properties.pop()
            if _a != a:
                a_less = True
                prev_d = d
                d = max(_d, prev_d)
                a = _a
            if a_less and _d < prev_d:
                res += 1

        # a, d, next_a, next_d = properties.pop()
        # while properties:
        #     _a, _d = properties.pop()
        #     if _a != next_a:
        #         a, next_a = next_a, _a
        #         d, next_d = max(d, next_d), _d
        #     if a > _a and d > _d: res += 1
        return res

if __name__ == "__main__":
    # properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
    properties = [[6, 9], [7, 5], [7, 9], [7, 10], [10, 4], [10, 7]]
    sol = Solution()
    print(sol.numberOfWeakCharacters(properties))

