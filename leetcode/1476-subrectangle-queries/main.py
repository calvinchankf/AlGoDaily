"""
    1st: better brute force
    - update the row by replacing a subarray (instead of replacing the cells one by one)

    Time of updateSubrectangle()    O(MN)
    Time of getValue()              O(1)
    252 ms, faster than 60.00%
"""


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        dump = (col2 - col1 + 1) * [newValue]
        for i in range(row1, row2+1):
            self.rect[i] = self.rect[i][:col1] + dump + self.rect[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]
