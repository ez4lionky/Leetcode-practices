class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isalpha():
                size += 1
            else:
                size *= int(ch)

        for c in s[::-1]:
            k %= size
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


if __name__ == "__main__":
    sol = Solution()
    # s = "leet2code3"
    # k = 10
    s = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
    k = 480551547
    print(sol.decodeAtIndex(s, k))

