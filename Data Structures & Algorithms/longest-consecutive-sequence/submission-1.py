from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSequence = 0
        numMap = defaultdict(lambda : 0)

        for num in nums:
            numMap[num] = 1

        for num in nums:
            currentSequence = 1
            while (num - 1) in nums:
                currentSequence += 1
                num -= 1
            if currentSequence > longestSequence:
                longestSequence = currentSequence
        return longestSequence