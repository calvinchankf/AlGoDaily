"""
    1st: just sort

    Time    O(NlogN)
    Space   O(N)
    280 ms, faster than 87.69%
"""


class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        if veganFriendly == 1:
            restaurants = [r for r in restaurants if r[2] == 1]

        arr = []
        for x in restaurants:
            if x[3] <= maxPrice and x[4] <= maxDistance:
                arr.append(x)

        sortedArr = sorted(arr, key=lambda x: (-x[1], -x[0]))

        return [x[0] for x in sortedArr]
