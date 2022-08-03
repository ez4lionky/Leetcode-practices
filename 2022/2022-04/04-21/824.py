class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        items = sentence.split()
        for i, item in enumerate(items):
            if item[0] in ['a', 'e', 'i', 'o', 'u']:
                item = item + 'ma' + 'a' * (i+1)
            else:
                item = item[1:] + item[0] + 'ma' + 'a' * (i+1)
            items[i] = item
        return ' '.join(items).strip()

if __name__ == "__main__":
    sol = Solution()
    sentence = "I speak Goat Latin"
    print(sol.toGoatLatin(sentence))

