"""
    1st: heap
    - negate the smallest number in K times

    Time    O(KlogN)
    Space   O(N)
    48 ms, faster than 69.71%
"""


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            smallest = heapq.heappop(A)
            heapq.heappush(A, -smallest)
        return sum(A)
