# seems like unoptimal, naive solution
# no hints
from collections import defaultdict

class Solution:
    def isSegmentValid(self, segment: List[str]):
        count = defaultdict(lambda : 0)

        for item in segment:
            count[item] += 1
        count["."] = 0

        for item, freq in count.items():
            if (freq > 1):
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.isSegmentValid(row):
                return False

        for column in zip(*board):
            if not self.isSegmentValid(column):
                return False

        for segment in range(9):
            y = segment // 3
            x = segment % 3
            segment = []
            for row in board[y * 3: (y + 1) * 3]:
                segment.extend(row[x * 3: (x + 1) * 3])

            if not self.isSegmentValid(segment):
                return False
        return True