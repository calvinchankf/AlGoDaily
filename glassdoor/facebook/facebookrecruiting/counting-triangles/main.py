"""
    Given a list of N triangles with integer side lengths, 
    determine how many different triangles there are. 
    
    Two triangles are considered to be the same if they can both be placed on the plane such that their vertices occupy exactly the same three points.

    Example 1
    arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
    output = 2
    The first two triangles are the same, so there are only 2 distinct triangles.
    
    Example 2
    arr = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
    output = 3
    All of these triangles are distinct.
    
    Example 3
    arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
    output = 1
    All of these triangles are the same.
"""


def countDistinctTriangles(arr):
    seen = set()
    for x in arr:
        a = sorted(list(x))
        seen.add(tuple(a))
    return len(seen)


# 2
a = [(2, 2, 3), (3, 2, 2), (2, 5, 6)]
print(countDistinctTriangles(a))

# 3
a = [(8, 4, 6), (100, 101, 102), (84, 93, 173)]
print(countDistinctTriangles(a))

# 1
a = [(5, 8, 9), (5, 9, 8), (9, 5, 8), (9, 8, 5), (8, 9, 5), (8, 5, 9)]
print(countDistinctTriangles(a))

# 3
a = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
print(countDistinctTriangles(a))

# 3
a = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
print(countDistinctTriangles(a))
