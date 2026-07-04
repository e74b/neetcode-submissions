class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSequence = 0

        for num in nums:
            currentSequence = 0
            while num in nums:
                currentSequence += 1
                num += 1

            if currentSequence > longestSequence:
                longestSequence = currentSequence
        return longestSequence