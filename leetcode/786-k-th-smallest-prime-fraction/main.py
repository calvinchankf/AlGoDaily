from heapq import heappush, heappop

"""
    1st: min heap
    - same logic as lc373
    - similar to lc23, 373, 378, 786
    - since the arrays are sorted, we dont have to consider all pairs
    we can just care if we can pop k smallest items out from the stack

    e.g.
    a = [1, 2, 3, 5]
    k = 3

    heap = [1/5, 2/5, 3/5, 5/5], consider the total of every element of nums / nums[n-1]
    
    count = 1, we pop the first one because it must be smallest one,
    1/5 (i=0, j=3) = heap.pop()
    heap = [2/5, 3/5, 5/5]
    then we consider adding nums[0] + nums[j-1 = 2] = 1/3 to the heap
    heap = [1/3, 2/5, 3/5, 5/5]

    count = 2, we pop the first one because it must be smallest one,
    1/3 (i=0, j=2) = heap.pop()
    heap = [2/5, 3/5, 5/5]
    then we consider adding nums[0] + nums[j-1 = 1] = 1/2 to the heap
    heap = [2/5, 1/2, 3/5, 5/5]

    count = 3, we pop the first one because it must be smallest one,
    2/5 (i=0, j=3) = heap.pop()
    since count == k, result = 2/5

    Time    O(N + KlogN)
    Space   O(N)
    3788 ms, faster than 30.40%
"""


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        pq = []
        for i in range(len(A)):
            x = A[i]
            y = A[n-1]
            heappush(pq, (x/y, i, n-1))
        count = 0
        while len(pq) > 0:
            _, i, j = heappop(pq)
            count += 1
            if count == K:
                return [A[i], A[j]]
            if j - 1 >= 0:
                x = A[i]
                y = A[j-1]
                heappush(pq, (x/y, i, j-1))
        return []
