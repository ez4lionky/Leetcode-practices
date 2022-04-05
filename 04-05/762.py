# class Solution:
#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         def isprime(n):
#             return (all([False for i in range(2,n) if n % i == 0 ]) and not n < 2)
#         res = 0
#         primes = set()
#         for n in range(left, right+1):
#             num_set = sum([int(b) for b in bin(n)[2:]])
#             # if isprime(num_set):
#             #     res += 1
#             if num_set in primes:
#                 res += 1
#             else:
#                 if isprime(num_set):
#                     primes.add(num_set)
#                     res += 1
#         return res


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))

