class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def mod(i, offset, n):
            return (i + offset) % n

        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            l, r = 1, k
        else:
            l, r = k, - 1

        w = sum(code[mod(0, l, n):mod(0, r, n)+1])
        res = [w]
        for i in range(1, n):
            w -= code[mod(i-1, l, n)]
            w += code[mod(i, r, n)]
            res.append(w)
        return res

