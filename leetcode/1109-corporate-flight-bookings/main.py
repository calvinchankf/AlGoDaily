"""
    1st: math
    - similar to lc732, l094, 1109, 1589, 1854
    - typical range frequency counting technique (line sweep) to deal with values on a range
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
        res = (n + 2) * [0]
        # range counting technique
        for i, j, k in bookings:
            res[i] += k
            res[j+1] -= k
        for i in range(1, n+1):
            res[i] += res[i-1]
        return res[1:-1]
