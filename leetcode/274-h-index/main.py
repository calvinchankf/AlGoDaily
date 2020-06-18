"""
    1st: upper bound binary search
    - find the first element whose value is more than the length of remaining array,
    so we return the remaining length as the answer.

    Time    O(logN)
    Space   O(1)
    32 ms, faster than 91.31% 
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        left = 0
        right = len(citations)
        while left < right:
            mid = (left + right)//2

            isNotMatched = citations[mid] < len(citations) - mid

            if isNotMatched:
                left = mid + 1
            else:
                right = mid
        return len(citations) - left
