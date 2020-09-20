"""
    0th: brute force
    Time    O(n^2)
    Space   O(n)
    LTE
"""

"""
    1st: math
    - similar to lcl094, 1589
    - typical range frequency counting technique to deal with values on a range
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval
    - ./idea.jpeg

    Time    O(2n)
    Space   O(n)
    784 ms, faster than 81.08%
"""


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = (n+1) * [0]
        for a, b, c in bookings:
            res[a-1] += c
            res[b] -= c
        for i in range(1, len(res)):
            res[i] += res[i-1]
        return res[:-1]
