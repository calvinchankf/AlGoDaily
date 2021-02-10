from heapq import *

"""
    1st: heap + hashtable
    - similar to lc373

    [1, 10, 10],
    [1,  4,  5],
    [2,  3,  6]

    the smallest sum is row[0][0] + row[1][0] + row[2][0] = 1+1+2
    then we consider the below 3 possibilities, which are the j + 1 for every row
    - row[0][1] + row[1][0] + row[2][0]
             *
    - row[0][0] + row[1][1] + row[2][0]
                         *
    - row[0][0] + row[1][0] + row[2][1]
                                     *

    Do it k times, then we will reach to the result

    catch: it is possible that there are duplicate combinations, so we can use a hashset

    Time    O(R + klogRC)
    Space   O(RC)
    144 ms, faster than 77.44%
"""


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        R, C = len(mat), len(mat[0])

        firstSum = 0
        for i in range(R):
            firstSum += mat[i][0]
        minheap = [(firstSum, R * [0])]

        seen = set()
        res = []
        while len(minheap) > 0:
            t, indices = heappop(minheap)
            # print(t, [mat[i][indices[i]] for i in range(R)])
            # print(t, [indices[i] for i in range(R)])
            res.append((t))
            if len(res) == k:
                break
            # put every row[j + 1] into the heap
            for i in range(R):
                j = indices[i]
                if j + 1 < C:
                    _t = t - mat[i][j] + mat[i][j+1]
                    _indices = indices[:]
                    _indices[i] += 1
                    key = tuple(_indices)
                    if key not in seen:
                        seen.add(key)
                        heappush(minheap, (_t, _indices))
        return res[-1]
