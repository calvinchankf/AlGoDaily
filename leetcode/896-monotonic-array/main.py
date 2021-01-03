"""
    questions to ask:
    - will the sequence contain less than 2 items? yes
    - will the numbers in the sequence are the same? yes e.g. [1,1,1,1,1,1,1]
"""


"""
    1st approach:
    1. check the polarity of the array from the begining
    2. check if the sequence follows the polarity

    Time    O(n)
    Space   O(1)
    472 ms, faster than 56.28%
"""


class Solution(object):
    def isMonotonic(self, A):
        isIncreasing = True
        isDecreasing = True
        for i in range(1, len(A)):
            diff = A[i] - A[i-1]
            if isIncreasing and diff < 0:
                isIncreasing = False
            if isDecreasing and diff > 0:
                isDecreasing = False
        return isIncreasing or isDecreasing


"""
    2nd approach:
    1. check the polarity by checking the front and the end of the input array. and reverse the array if decreasing
    2. check if the sequence is monotonic increasing

    Time    O(n)
    Space   O(1)
    440 ms, faster than 32.12%
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return True

        if A[0] > A[-1]:
            A = A[::-1]

        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
