from typing import List
import heapq

"""
    2nd: heap
    - we dont have to iterate all the subarrays, we just need to iterate the first RIGHT with a minheap

    e.g. [4,2,1,3], 1, 4

    sorted = [1,2,3,4]
    
    start         total= 0,    [(1, 0), (2, 1), (3, 2), (4, 3)]             
    i = 0, pop=1, total=0+1=1, [(2, 1), (1+2, 2), (3, 2), (4, 3)]
    i = 1, pop=2, total=1+2=3, [(1+2, 2), (3, 2), (4, 3), (2+3, 2)]
    i = 2, pop=3, total=3+3=6, [(3, 2), (4, 3), (5, 2), (1+2+3, 2)]
    i = 3, pop=3, total=6+3=9, [(4, 3), (5, 2), (1+2+3, 2), (3+4, 3)]
    ...(go on or stop depends on how big is RIGHT)...

    ref:
    - https://www.youtube.com/watch?v=6UJEMVmMJDw

    Time    O(RlogN) -> O(X^logX) N=len(nums), R=right, X=N^2
    56 ms, faster than 83.33%
"""


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(pq)

        res = 0
        for i in range(1, right + 1):
            x, idx = heapq.heappop(pq)
            if i >= left:
                res += x % (10**9 + 7)
            if idx + 1 < len(nums):
                heapq.heappush(pq, (x + nums[idx+1], idx + 1))
        return res


s = Solution()

a = [1, 2, 3, 4]
print(s.rangeSum(a))
