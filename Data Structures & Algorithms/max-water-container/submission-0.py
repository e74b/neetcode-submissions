class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while  left < right:
            # maximizes W, what about H
            currentArea = min(heights[left], heights[right]) * (right - left)
            if maxArea < currentArea:
                maxArea = currentArea

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea