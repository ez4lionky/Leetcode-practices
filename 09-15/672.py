class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # the light status will be periodic and the presses status have only two possible value.
        ops = [0b111111, 0b010101, 0b101010, 0b100100]
        n = min(6, n)
        results = set()
        for press in range(1 << 4):
            cnt = press.bit_count()
            if cnt <= presses and cnt % 2 == presses % 2:
                final_press = 0
                for i, op in enumerate(ops):
                    if (press >> i) & 1:
                        final_press ^= op
                result = (1 << 6) - 1
                result &= final_press
                result >>= (6 - n)
                results.add(result)
        return len(results)

