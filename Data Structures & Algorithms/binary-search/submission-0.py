class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        base = 0

        while not found:
            mid = nums[len(nums) // 2]
            if mid == target:
                return base + (len(nums) // 2)
            if len(nums) == 1:
                return -1
            if mid > target:
                nums = nums[:(len(nums) // 2)]
                continue
            if mid < target:
                base += len(nums) // 2
                nums = nums[(len(nums) // 2):]
                continue
                