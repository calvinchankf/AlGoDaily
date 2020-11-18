"""
    1st: binary search
    - similar to lc926, 1653

    The intuition is that, let's say you have '00101101'
    indices of all the '0'
    A = [0,1,3,6]
    indices of all the '1'
    B = [2,4,5,7]
    We want to delete the tail of A or the head of B, so that all the numbers in A are larger than B.
    i.e. A = [0,1,3], B = [4,5,7]
    Since the indices are sorted, we can loop over A and binary search a point where B[j] > A[i] in B

    Time    O(N + AlogB) i.e. A+B = N
    Space   O(N)
    124 ms, faster than 13.01%
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        A = [-1]  # consider '1110', u want to delete the 0 instead of 111
        B = []
        for i in range(len(S)):
            c = S[i]
            if c == '0':
                A.append(i)
            else:
                B.append(i)
        res = 2**31 - 1
        for i in range(len(A)):
            a = A[i]
            j = self.upperBoundbsearch(B, a)
            toDeleteInA = len(A) - i - 1
            toDeleteInB = j
            charsToDelete = toDeleteInA + toDeleteInB
            res = min(res, charsToDelete)
        if res == 2**31 - 1:  # or sys.maxsize / 'inf', whatever
            return 0
        return res

    # or python bisect right, whatever
    def upperBoundbsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


"""
    2nd: stack
    - similar to lc926, 1653
    - the idea is whenever you see a 0, remove the previous 1 if there is
    
    e.g. '0010110'
                0 0 1 0 1 1 0
    # of ones   0 0 1 0 1 2 1
    -------------------------
    result      0 0 0 1 1 1 2

    ref:
    https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183896/Prefix-Suffix-Java-O(N)-One-Pass-Solution-Space-O(1)

    Time    O(N)
    Space   O(1)
    32 ms, faster than 100.00%
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        b = 0
        res = 0
        for i in range(len(S)):
            if S[i] == '1':
                b += 1
            elif S[i] == '0':
                if b > 0:
                    b -= 1
                    res += 1
        return res
