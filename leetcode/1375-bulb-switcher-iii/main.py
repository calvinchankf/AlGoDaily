"""
    Approach: array
    - keep track of the right-most bulb
    - whenever the right-most bulb equals i + 1 we know all bulbs are blue

    Time    O(N)
    Space   O(1)
    396 ms, faster than 65.91%
"""


class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        right = res = 0
        for i, a in enumerate(light, 1):
            right = max(right, a)
            res += right == i
        return res
