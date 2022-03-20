class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        n, ds, s_p = len(directions), list(directions), []
        i = 0
        while i < n:
            if i<n-1 and ds[i] == 'R' and ds[i+1] == 'L':
                res += 2
                ds[i] = 'S'
                ds[i+1] = 'S'
                s_p.append(i)
                s_p.append(i+1)
                i += 2
            else:
                if ds[i] == 'S':
                    s_p.append(i)
                i+=1
        if len(s_p) == 0:
            return 0
        for i in range(n):
            if ds[i] == 'R' and s_p[-1] > i:
                res += 1
            if ds[i] == 'L' and s_p[0] < i:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # directions = "RLRSLL"
    # directions = "LLRR"
    directions = "SRRLRLRSRLRSSRRLSLRLLRSLSLLSSRRLSRSLSLRRS"
    print(sol.countCollisions(directions))

