class Solution:
    code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = 0
        coded_set = set()
        for w in words:
            morse_code = ''
            for c in w:
                idx = ord(c) - ord('a')
                morse_code += self.code[idx]
            if morse_code not in coded_set:
                res += 1
                coded_set.add(morse_code)
        return res

