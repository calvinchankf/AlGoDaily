from typing import List
from functools import cmp_to_key

"""
    1st: custom sort
    - take away: functools.cmp_to_key

    Time    O(2 * NlogN)
    Space   O(N)
    2276 ms, faster than 18.90%
"""


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n-1)//2]

        def compare(a, b):
            diff = abs(a - median) - abs(b - median)
            if diff > 0:
                return diff
            return a - b

        res = sorted(arr, key=cmp_to_key(
            lambda a, b: compare(a, b)), reverse=True)
        return res[:k]


"""
    2nd: sort + 2 pointers

    Time    O(NlogN + k)
    Space   O(k)
    1348 ms, faster than 82.00%
"""


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        median = arr[(n-1)//2]
        left, right = 0, n-1
        res = []
        for _ in range(k):
            if arr[right] - median >= median - arr[left]:
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
        return res
