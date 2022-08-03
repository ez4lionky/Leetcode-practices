class MagicDictionary:

    def __init__(self):
        self.dict = set()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict.add(word)
        return


    def search(self, searchWord: str) -> bool:
        for word in self.dict:
            if len(word) == len(searchWord):
                if sum(word[i]!=searchWord[i] for i in range(len(word))) == 1:
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
