class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        for i in range(len(words)):
            for j in range(1, len(words[i])+1):
                if words[i][:j] in dictionary:
                    words[i] = words[i][:j]
                    break
            
        return ' '.join(words)

