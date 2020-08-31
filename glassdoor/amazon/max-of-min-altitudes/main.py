import sys

"""
    Given a matrix with r rows and c columns, 
    find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. 
    The score of a path is the minimum value in that path. 
    For example, the score of the path 8 -> 4 -> 5 -> 9 is 4.

    Don't include the first or final entry. You can only move either down or right at any point in time.
    
    ------------------------------------------------------------------------
    Example 1:

    Input:
    [[5, 1],
    [4, 5]]

    Output: 4
    
    Explanation:
    Possible paths:
    5 -> 1 -> 5 => min value is 1
    5 -> 4 -> 5 => min value is 4
    Return the max value among minimum values => max(4, 1) = 4.
    ------------------------------------------------------------------------
    Example 2:

    Input:
    [[1, 2, 3]
    [4, 5, 1]]

    Output: 4
    
    Explanation:
    Possible paths:
    1-> 2 -> 3 -> 1
    1-> 2 -> 5 -> 1
    1-> 4 -> 5 -> 1
    So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
    Return the max of that, so 4.
    ------------------------------------------------------------------------

    ref:
    - https://leetcode.com/discuss/interview-question/383669/
"""


def maxOfMinAltitudes(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    R = len(matrix)
    C = len(matrix[0])
    scores = []
    for _ in range(R):
        scores.append(C * [sys.maxsize])

    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                scores[i][j] = min(matrix[i][j], scores[i][j-1])
            elif j == 0:
                scores[i][j] = min(matrix[i][j], scores[i-1][j])
            else:
                scores[i][j] = max(
                    min(matrix[i][j], scores[i-1][j]),
                    min(matrix[i][j], scores[i][j-1])
                )
    return max(scores[R-1][C-2], scores[R-2][C-1])


# 4
a = [[5, 1],
     [4, 5]]
print(maxOfMinAltitudes(a))

# 4
a = [[1, 2, 3],
     [4, 5, 1]]
print(maxOfMinAltitudes(a))

# 5
a = [[6, 7, 8],
     [5, 4, 2],
     [8, 7, 6]
     ]
print(maxOfMinAltitudes(a))
