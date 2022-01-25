# vanilla version: simulate matches
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         n_matches = 0
#         while n != 1:
#             quotient, remainder = divmod(n, 2)
#             n = quotient + remainder
#             n_matches += quotient
#         return n_matches


# find the regular pattern: we need to eliminate n-1 teams and left only one team to win
# and one match will eliminate one team
# thus n-1 matches need to play

# another way: f(1) = 0; f(n) = 1 + f(n-1); f(n)+f(n−1)+…+f(1)=1+f(n−1)+1+f(n−2)+…+1+f(1)+0
# thus f(n) = n - 1
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == "__main__":
    sol = Solution()
    for i in range(1, 201):
        print(f'{i}: ', sol.numberOfMatches(i))

