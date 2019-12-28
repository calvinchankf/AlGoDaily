"""
    1st: dynamic programming
    - top down recursion + hashtable

    ref:
    - https://www.youtube.com/watch?v=1UW3SxuITKs

    Time    O(N^2)
    Space   O(N^2)
    152 ms, faster than 10.87%
"""


class Solution(object):

    def __init__(self):
        self.ht = {}

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N in self.ht:
            return self.ht[N]
        for i in range(1, N):
            if N % i == 0:
                if self.divisorGame(N-i) == False:
                    self.ht[N] = True
                    return True
        self.ht[N] = False
        return False


"""
    2nd: math
    - not recommend

    ref:
    - https://leetcode.com/problems/divisor-game/discuss/274606/JavaC%2B%2BPython-return-N-2-0
"""


class Solution(object):
    def divisorGame(self, N):
        return N % 2 == 0
