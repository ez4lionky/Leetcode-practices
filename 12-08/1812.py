class Solution:
    def __init__(self) -> None:
        self.s = set()
        for i in range(1,9):
            for c in range(ord('a'), ord('i')):
                if (i % 2) == (c % 2):
                    self.s.add(chr(c)+str(i))
        return

    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates in self.s:
            return False
        return True
        
