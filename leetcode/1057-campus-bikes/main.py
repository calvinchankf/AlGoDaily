import heapq

"""
    quesions to ask:
    - len(workers) != len(bikes)? yes, but len(workers) must be <= len(bikes)

"""

"""
    1st approach: min heap + hashtable

    Time    O(2WBlogWB) heap sort, heap pops
    Space   O(WB)
    LTE wtf?
"""


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        pq = []
        for bIdx in range(len(bikes)):
            x, y = bikes[bIdx]
            for wIdx in range(len(workers)):
                a, b = workers[wIdx]
                dist = abs(x - a) + abs(y - b)
                pq.append((dist, wIdx, bIdx))
        heapq.heapify(pq)
        bUsed = set()
        wUsed = set()
        res = len(workers) * [-1]
        while len(pq) > 0:
            d, w, b = heapq.heappop(pq)
            if b in bUsed or w in wUsed:
                continue
            bUsed.add(b)
            wUsed.add(w)
            res[w] = b
        return res


s = Solution()

a = [[0, 0], [2, 1]]
b = [[1, 2], [3, 3]]
print(s.assignBikes(a, b))

a = [[0, 0], [1, 1], [2, 0]]
b = [[1, 0], [2, 2], [2, 1]]
print(s.assignBikes(a, b))

print("-----")


"""
    2nd  approach: sort + hashtable
    - in python, if we do sorting, [(a0, b0, c0), (a1, b1, c1)...], all tuples are sorted, 
    so we dont need a custom comparator like below:

    def cptr(a, b):
        if a[0] == b[0] and a[1] == b[1]:
            return a[2]-b[2]
        elif a[0] == b[0]:
            return a[1]-b[1]
        return a[0]-b[0]

    Time    O(WBlogWB)
    Space   O(WB)
    1848 ms, faster than 18.51%
"""


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # get all the combinations
        pq = []
        for bidx in range(len(bikes)):
            x, y = bikes[bidx]
            for widx in range(len(workers)):
                a, b = workers[widx]
                dist = abs(x - a) + abs(y - b)
                pq.append((dist, widx, bidx))
        # sort the distances order by workerIdx, bikeIdx
        pq.sort()
        bUsed = set()
        wUsed = set()
        res = len(workers) * [-1]
        # construct results
        for d, w, b in pq:
            if b in bUsed or w in wUsed:
                continue
            bUsed.add(b)
            wUsed.add(w)
            res[w] = b
        return res


s = Solution()

a = [[0, 0], [2, 1]]
b = [[1, 2], [3, 3]]
print(s.assignBikes(a, b))

a = [[0, 0], [1, 1], [2, 0]]
b = [[1, 0], [2, 2], [2, 1]]
print(s.assignBikes(a, b))

print("-----")
