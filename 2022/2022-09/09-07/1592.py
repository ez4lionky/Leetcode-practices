class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_num = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * space_num
        per_space, rest_space = divmod(space_num, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * rest_space

