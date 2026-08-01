class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        else:
            triangleTop = self.generate(numRows - 1)
            bottomRow = triangleTop[-1]
            offsetRow = triangleTop[-1][1:]

            currentRow = []
            for x, y in zip(bottomRow, offsetRow):
                currentRow.append(x + y)
            currentRow = [1, *currentRow, 1]
        return [*triangleTop, currentRow]