"""
    1st approach: 2 pointers
    1  1 pointer for arrayA, 2 pointer for arrB
    2. extract the overlapping time from A[p1] , B[p2] by using
        s = max(s1, s2)
        e = min(e1, e2)
    3. move forward the pointer in which the interval has minimum end time

    e.g.1
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]

    [0,2], [1,5] => [1, 2] then p1 += 1
    [5, 10], [1, 5] => [5, 5] then p2 += 1
    [5, 10], [8, 12] => [8, 10] then p1 += 1
    [13, 23], [8, 12] => [13, 12] dont consider, then p2 += 1
    [13, 23], [15, 24] => [15, 23] then p1 += 1
    [24, 25], [15, 24] => [24, 24] then p2 += 1
    [24, 25], [25, 26] => [25, 25] then p1 += 1

    result = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    e.g.2
    A = [[0,10], [20,30], [31,32]]
    B = [[1,2], [3,4], [5,6], [10, 12], [19,30], [31,33]]
    
    [0,10], [1,2] => [1,2] then p2 += 1
    [0,10], [3,4] => [3,4] then p2 += 1
    [0,10], [5,6] => [5,6] then p2 += 1
    [0,10], [10,12] => [10, 10] then p2 += 1
    [20,30], [10,12] => [20, 12] dont consider, then p2 += 1
    [20,30], [19,30] => [20, 30] then p2 += 1
    [20,30], [31,33] => [31, 30] dont consider, then p1 += 1
    [31,32], [31,33] => [31, 32] then p1 += 1, finish

    result = [[1,2],[3,4],[5,6],[10,10],[20,30],[31,32]]


    Time    O(A+B)
    Space   O(A+B)
    160 ms, faster than 67.18%
"""


class Solution(object):
    def intervalIntersection(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return []
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(A) and p2 < len(B):
            s1, e1 = A[p1]
            s2, e2 = B[p2]
            a = max(s1, s2)
            b = min(e1, e2)
            if a <= b:
                res.append([a, b])
            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return res
