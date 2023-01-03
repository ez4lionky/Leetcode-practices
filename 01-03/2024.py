class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        items = s.split()
        pre, cur = None, None
        for item in items:
            if item.isdigit():
                if pre is None and cur is None:
                    pre, cur = 0, int(item)
                else:
                    pre, cur = cur, int(item)
                    if pre >= cur:
                        return False
        return True


