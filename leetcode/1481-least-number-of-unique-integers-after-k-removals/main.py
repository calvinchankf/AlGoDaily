from collections import Counter
import heapq

"""
    1st: hashtable + minheap
    - calculate the occurance of every number
    - use minheap to remove the least appeared number until k = 0

    Time    O(NlogN)
    Space   O(N)
    1004 ms, faster than 33.33%
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ht = Counter(arr)
        minHeap = []
        for key in ht:
            occur = ht[key]
            heapq.heappush(minHeap, (occur, key))

        while len(minHeap) > 0:
            if k == 0:
                break
            occur, key = heapq.heappop(minHeap)
            if k >= occur:
                k -= occur
            else:
                k = 0
                heapq.heappush(minHeap, (occur-k, key))

        return len(minHeap)
