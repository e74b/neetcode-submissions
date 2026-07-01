class Solution:
    def hashWord(self, word):
        wordHash = [0] * 26
        for letter in word:
            wordHash[ord(letter) - ord('a')] += 1

        return tuple(wordHash)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordGroups = {}

        for word in strs:
            wordHash = self.hashWord(word)
            if wordHash in wordGroups:
                wordGroups[wordHash].append(word)
            else:
                wordGroups[wordHash] = [word]

        return list(wordGroups.values())