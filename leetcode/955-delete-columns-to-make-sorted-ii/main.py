"""
    1st: brute force
    - initial N empty strings
    - for each column, add a character on each row
    - check if all rows are still sorted

    Time    O(RC)
    Space   O(RC)
    48ms beats 22.22%
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r = len(A)
        c = len(A[0])
        strs = [""] * r
        res = 0
        for j in range(c):

            clone = strs[:]
            for i in range(r):
                clone[i] += A[i][j]

            isBroken = False
            for k in range(1, r):
                if clone[k-1] > clone[k]:
                    isBroken = True
                    break

            if isBroken:
                res += 1
            else:
                strs = clone

        return res


s = Solution()
a = ["cfxc", "beyb", "adza"]
print(s.minDeletionSize(a))
