class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstHash = {}
        secondHash = {}

        for letter in s:
            if letter not in firstHash:
                firstHash[letter] = 0
            firstHash[letter] += 1

        for letter in t:
            if letter not in secondHash:
                secondHash[letter] = 0
            secondHash[letter] += 1

        return (firstHash == secondHash)