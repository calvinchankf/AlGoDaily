"""
    https://leetcode.com/discuss/interview-question/370988/Amazon-or-Phone-Screen-or-Count-Number-of-Squares-in-a-grid

    Find a total number of overlapping squares in a given gird.

    e.g.
    **
    **
    Above matrix should return 5 as it is having 5 total squares in it (each star forms one square and all four stars form one square).

    e.g.
    ****
    ****
    ****
    return 20

    e.g.
    ***
    ***
    ***
    ***
    return 20

    e.g.
    ***
    ***
    ***
    ***
    ***
    return 26
"""


def countSquaresInGrid(R, C):
    res = 0
    for i in range(R):
        temp = 0
        for j in range(C):
            temp += min(R-i, C-j)
        res += temp
    return res


print(countSquaresInGrid(2, 2))
print(countSquaresInGrid(3, 4))
print(countSquaresInGrid(4, 3))
print(countSquaresInGrid(5, 3))
