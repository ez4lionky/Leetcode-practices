class Solution:
    def defangIPaddr(self, address: str) -> str:
        # items = address.split('.')
        # return '[.]'.join(items)
        return address.replace('.', '[.]')


if __name__ == "__main__":
    address = "1.1.1.1"
    sol = Solution()
    print(sol.defangIPaddr(address))

