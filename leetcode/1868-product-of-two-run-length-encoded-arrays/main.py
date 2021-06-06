"""
    1st: two pointers
    - similar to leetcode 4, 21, 23

    Time    O(N)
    Space   O(N)
    2844 ms, faster than 41.54%
"""


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]

            f = min(f1, f2)
            v = v1*v2

            if len(res) > 0 and res[-1][0] == v:
                res[-1][1] += f
            else:
                res.append([v, f])

            encoded1[i][1] -= f
            encoded2[j][1] -= f

            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return res
