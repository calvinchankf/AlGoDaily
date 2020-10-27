"""
    Given 2 arrays, sort the first array in a way that numbers 
    whose indeces exist in the second array stay unmoved and all other numbers are sorted
    
    e.g. [6, 5, 4, 3, 2, 1], [0, 3, 5]
    Output: [6, 2, 4, 3, 5, 1]
    Explanation: 
     0  1  2  3  4  5
    [6, 5, 4, 3, 2, 1]
     ^        ^     ^
    
    [6, _, _, 3, _, 1] <- these numbers stay unmoved
    [6, 2, 4, 3, 5, 1] <- sort [5, 4, 2] and put them into those slots
"""
def solve(arr1, arr2):
    hs = set(arr2)
    cands = []
    for i in range(len(arr1)):
        if i not in hs:
            cands.append(arr1[i])
    cands.sort()
    res = arr1[:]
    for i in range(len(arr1)):
        if i not in hs:
            res[i] = cands.pop(0)
    return res

a = [6, 5, 4, 3, 2, 1]
b = [0, 3, 5]
print(solve(a, b))