"""
    1st approach: math + hashtable
    - we only need to consider each song length modulo 60
    - we can count the number of songs with (length % 60) equal to r, and store that in an array of size 60

    e.g. [60, 60, 20, 40, 100, 63]
    cache[0] = 2
    cache[3] = 1
    cache[20] = 1
    cache[40] = 2

    cache[0] can pair with cache[0]
    cache[20] can pair with cache[40]
    ....etc

    Time    O(n)
    Space   O(n)
    196 ms, faster than 56.37%
"""


class Solution(object):
    def numPairsDivisibleBy60(self, times):
        """
        :type time: List[int]
        :rtype: int
        """
        cache = 60 * [0]
        res = 0
        for t in times:
            r = t % 60
            partner = (60 - r) % 60
            if cache[partner] > 0:
                res += cache[partner]
            cache[r] += 1
        return res
