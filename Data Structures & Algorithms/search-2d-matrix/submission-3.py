class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = []
        for item in matrix:
            row.extend(item)
        return target in row
        
        ##  disregarding the problem,just a sanity check
        right = len(matrix) - 1
        left = 0
        mid: int | None = None


        while True:
            mid = (right + left) // 2
            rangeStart = matrix[mid][0]
            rangeEnd = matrix[mid][-1]

            if target < rangeStart:
                right = mid
                break
            elif target > rangeEnd:
                left = mid
                break
            elif rangeStart <= target <= rangeEnd:
                break

            if (right - left) <= 1:
                return False
        importantRowIndex = mid

        left = 0
        right = len(matrix[importantRowIndex])

        while (right - left) >= 1:
            mid = (right + left) // 2
            if matrix[importantRowIndex][mid] == target:
                return True
            elif matrix[importantRowIndex][mid] > target:
                right = mid
            else:
                left = mid

        return False