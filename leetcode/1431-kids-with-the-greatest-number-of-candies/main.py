"""
    1st: find max

    Time    O(N)
    Space   O(N) <- the result array
    36 ms, faster than 33.33%
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = max(candies)
        return [x + extraCandies >= maxCan for x in candies]
