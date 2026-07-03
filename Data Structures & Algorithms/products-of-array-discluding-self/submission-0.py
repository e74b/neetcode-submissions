class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # taken 3 hints
        prefix = []
        suffix = []

        prefixProduct = 1
        for element in nums:
            prefix.append(prefixProduct)
            prefixProduct *= element

        suffixProduct = 1
        for element in reversed(nums):
            suffix.append(suffixProduct)
            suffixProduct *= element

        suffix = list(reversed(suffix))

        return [
            prefix * suffix
            for (prefix, suffix) in zip(prefix, suffix)
            ]