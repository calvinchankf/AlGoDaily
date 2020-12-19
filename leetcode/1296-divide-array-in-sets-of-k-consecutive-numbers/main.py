from heapq import *
from collections import defaultdict

"""
    1st: sort + hashtable
    1. sort the array
    2. put the indexes in a hashtable for every number
    3. for each unseen number, try to see if we can form a sequence(in length of K)

    Time    O(NlogN + NK)
    Space   O(N)
    564 ms, faster than 21.12%
"""


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        ht = defaultdict(list)
        for i in range(len(nums)):
            ht[nums[i]].append(i)
        seen = set()
        for i in range(len(nums)):
            if i in seen:
                continue
            seen.add(i)
            cur = nums[i]
            for _ in range(k-1):
                nex = cur + 1
                if nex in ht and len(ht[nex]) > 0:
                    j = ht[nex].pop(0)
                    seen.add(j)
                    cur = nex
                else:
                    return False
        return True


"""
    2nd: heap
    - sort the array
    - keep adding a current item into a list from the heap if list[0] + 1 == current
    - if a list is of length k, put that into a cache
    - the overall items in the cache should be N

    Time    O(NlogN + NlogK)
    Space   O(N)
    496 ms, faster than 21.89%
"""


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        minheap = []
        res = []
        for x in nums:
            if len(minheap) > 0 and minheap[0][0] + 1 == x and len(minheap[0][1]) < k:
                head, arr = heappop(minheap)
                arr.append(x)
                if len(arr) == k:
                    res.append(arr)
                else:
                    heappush(minheap, (x, arr))
            else:
                heappush(minheap, (x, [x]))
        count = 0
        for arr in res:
            count += len(arr)
        return count == len(nums)
