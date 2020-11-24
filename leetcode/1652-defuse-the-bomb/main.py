"""
    Array + math
    - i hate calculation for indices

    Time    O(N)
    Space   O(N)
    28 ms, faster than 100.00%
"""


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k > 0:
            nextKSum = sum(code[:k])
            nextKSums = []
            for i in range(n-1, -1, -1):
                nextKSums.append(nextKSum)
                nextKSum -= code[(i+k) % n]
                nextKSum += code[i]
            return nextKSums[::-1]
        if k < 0:
            k_ = -k
            prevKSum = sum(code[n-k_:])
            prevKSums = []
            for i in range(n):
                prevKSums.append(prevKSum)
                prevKSum -= code[i-k_]
                prevKSum += code[i]
            return prevKSums
        return n * [0]
