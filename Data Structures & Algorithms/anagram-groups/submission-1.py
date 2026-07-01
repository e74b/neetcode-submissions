class Solution:
    def hashWord(self, word):
        return "".join(sorted([letter for letter in word]))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lut = {}
        for word in strs:
            wordhash = self.hashWord(word)
            if wordhash not in lut:
                lut[wordhash] = [word]
            else:
                lut[wordhash].append(word)

        return list(lut.values())