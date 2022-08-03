class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word[:i+1][::-1] + word[i+1:]


if __name__ == "__main__":
    word = "abcdefd"
    ch = "d"
    sol = Solution()
    print(sol.reversePrefix(word, ch))

