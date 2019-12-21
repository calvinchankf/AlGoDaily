"""
    It is lc1253: Reconstruct a 2-Row Binary Matrix
"""


def solution(upper, lower, colsum):
    # write your code in Python 3.6
    n = len(colsum)
    row1 = n * [0]
    row2 = n * [0]
    for i in range(n):
        if colsum[i] == 2:
            if upper > 0 and lower > 0:
                row1[i] = 1
                row2[i] = 1
                upper -= 1
                lower -= 1
            else:
                return []
    for i in range(n):
        if colsum[i] == 1:
            if upper > 0:
                row1[i] = 1
                upper -= 1
            elif lower > 0:
                row2[i] = 1
                lower -= 1
            else:
                return []
    if upper == 0 and lower == 0:
        return [row1, row2]
    return []


print(solution(3, 2, [2, 1, 1, 0, 1]))
