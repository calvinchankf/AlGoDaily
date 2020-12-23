from heapq import *
from collections import defaultdict

"""
    1st: sort + hashtable
    - put every number counter
    - sort the array
    - for each unused number, try to see if we can form a sequence(in length of K)
    
    Time    O(NlogN + NK)
    Space   O(N)
    612 ms, faster than 12.45%
"""


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        counter = Counter(nums)
        for i in range(len(nums)):
            x = nums[i]
            if x not in counter:
                continue
            seq = [x]
            cur = x
            counter[cur] -= 1
            if counter[cur] == 0:
                del counter[cur]
            while cur+1 in counter and len(seq) < k:
                cur += 1
                seq.append(cur)
                counter[cur] -= 1
                if counter[cur] == 0:
                    del counter[cur]
            if len(seq) != k:
                return False
        return True


"""
    2nd: min heap
    - exactly the same as lc846
    - sort the array
    - keep adding a current item into a list from the heap if list[0] + 1 == current
    - if a list is of length k, put that into a cache
    - the overall items in the cache should be N

    corner case: nums = [1,2,3], k = 1

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
                if k == 1:
                    res.append([x])
                else:
                    heappush(minheap, (x, [x]))
        return len(minheap) == 0
