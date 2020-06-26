"""
    Approach: ???
    1. find the index of the largest number
    2. reverse arr[i]

    e.g.
    3, 2, 4, 1
          ^
    4, 2, 3, 1 <- 3
    1, 3, 2, 4 <- 4
       ^
    3, 1, 2, 4 <- 2
    2, 1, 3, 4 <- 3
    ^
    2, 1, 3, 4 <- 1
    1, 2, 3, 4 <- 2


    44 ms, faster than 19.39%
"""


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = []
        for x in range(N, 1, -1):
            i = A.index(x)
            res.append(i+1)
            res.append(x)

            sub = A[:i+1]
            A = sub[::-1] + A[i+1:]

            sub = A[:x]
            A = sub[::-1] + A[x:]
        return res


s = Solution()

a = [3, 2, 4, 1]
print(s.pancakeSort(a))
