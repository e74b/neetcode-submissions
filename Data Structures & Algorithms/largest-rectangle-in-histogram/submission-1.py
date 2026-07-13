class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areaMax = 0

        for c, currentHeight in enumerate(heights):

            maxRightTraversal = 0
            for newHeight in heights[c:]:
                if newHeight < currentHeight:
                    break
                else:
                    maxRightTraversal += 1

            maxLeftTraversal = 0

            for newHeight in heights[:c][::-1]:
                if newHeight < currentHeight:
                    break
                else:
                    maxLeftTraversal += 1

            area = (maxLeftTraversal + maxRightTraversal) * currentHeight

            if area > areaMax:
                areaMax = area
        return areaMax