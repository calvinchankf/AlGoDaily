"""
    1st: brute force
    1. push every stone to the right
    2. rotate the matrix

    Time    O(RCC)
    Space   O(RC)
    4756 ms, faster than 16.33%
"""


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R, C = len(box), len(box[0])
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                if box[i][j] == '#':
                    _j = j
                    while _j+1 < C and box[i][_j+1] == '.':
                        box[i][_j] = '.'
                        box[i][_j+1] = '#'
                        _j += 1
        return self.rotate(box)

    def rotate(self, box):
        R, C = len(box), len(box[0])
        matrix = []
        for j in range(C):
            matrix.append(R * [''])
        for i in range(R):
            for j in range(C):
                matrix[j][R-1-i] = box[i][j]
        return matrix
