# class Solution:
#     def countValidWords(self, sentence: str) -> int:
#         def valid(s: str) -> bool:
#             hasHyphens = False
#             for i, ch in enumerate(s):
#                 if ch.isdigit() or ch in "!.," and i < len(s) - 1:
#                     return False
#                 if ch == '-':
#                     if hasHyphens or i == 0 or i == len(s) - 1 or not s[i - 1].islower() or not s[i + 1].islower():
#                         return False
#                     hasHyphens = True
#             return True
#
#         return sum(valid(s) for s in sentence.split())


class Solution:
    @staticmethod
    def is_word(string):
        has_hyphens = False
        if len(string) == 0:
            return False
        for i, s in enumerate(string):
            if s.isdigit() or s in "!.," and i < len(string) - 1:
                return False
            if s == '-':
                if has_hyphens or i == 0 or i == len(string) - 1 or not string[i-1].islower or not string[i+1].islower():
                    return False
                has_hyphens = True
        return True

    def countValidWords(self, sentence: str) -> int:
        # one word has only one punctuation and only can be put on the end
        # no digits
        items = sentence.split(' ')
        return sum(self.is_word(item) for item in items)


if __name__ == "__main__":
    sol = Solution()
    sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    print(sol.countValidWords(sentence))

