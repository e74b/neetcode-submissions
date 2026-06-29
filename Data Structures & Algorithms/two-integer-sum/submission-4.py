class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for c, number in enumerate(nums):
            pair = target - number
            if pair in table:
                return [table[pair], c]
            
            table[number] = c
