"""
    1st: math
    - similar to lc1109, 1589
    - typical range counting technique to deal with values on a range
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval

    Time    O(2n)
    Space   O(n)
    48 ms, faster than 71.10%
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips = sorted(trips, key=lambda x: x[1])

        maxIdx = max([x[2] for x in trips])
        slots = (maxIdx+1) * [0]  # or slots = 1001 * [0] according to the desc

        for num, start, end in trips:
            slots[start] += num
            slots[end] -= num
        cur = 0
        for i in range(len(slots)):
            cur += slots[i]
            if cur > capacity:
                return False
        return True


s = Solution()

a = [[5, 4, 7], [7, 4, 8], [4, 1, 8]]
b = 17
print(s.carPooling(a, b))
