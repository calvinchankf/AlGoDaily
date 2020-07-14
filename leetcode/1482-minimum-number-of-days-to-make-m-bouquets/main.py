"""
    1st: binary search
    - from 1st to Nth day, there must be a day that we can make at least m bouquets
        FFFFTTTTTT F: false, T: true
    - we can do a lower bound binary search to look for the first True

    Time    O(NlogN)
    Space   O(1)
    1444 ms, faster than 95.66% 
"""


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        left = 1
        right = max(bloomDay)
        while left < right:
            mid = (left + right)//2

            ifSucceeded = False
            bouquetsCount = 0
            adjacent = 0
            for x in bloomDay:
                if x <= mid:
                    adjacent += 1
                else:
                    adjacent = 0
                if adjacent == k:
                    adjacent = 0
                    bouquetsCount += 1
                    if bouquetsCount == m:
                        ifSucceeded = True
                        break

            if ifSucceeded:
                right = mid
            else:
                left = mid + 1
        return left
