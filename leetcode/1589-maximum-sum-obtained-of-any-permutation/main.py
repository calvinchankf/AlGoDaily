"""
    0th: brute force

    Time    O(N^2 + NlogN)
    LTE
"""


import heapq


class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        counts = n * [0]
        for s, e in requests:
            for i in range(s, e+1):
                counts[i] += 1

        nums.sort(reverse=True)
        pq = [(counts[i], i) for i in range(n)]
        pq.sort(reverse=True)
        ht = {}
        while len(pq) > 0:
            c, i = pq.pop(0)
            x = nums.pop(0)
            ht[i] = x

        res = 0
        for s, e in requests:
            for i in range(s, e+1):
                res += ht[i]
        return res % (10**9+7)


s = Solution()

a = [1, 2, 3, 4, 5]
b = [[1, 3], [0, 1]]
print(s.maxSumRangeQuery(a, b))

a = [1, 2, 3, 4, 5, 6]
b = [[0, 1]]
print(s.maxSumRangeQuery(a, b))


a = [1, 2, 3, 4, 5, 10]
b = [[0, 2], [1, 3], [1, 1]]
print(s.maxSumRangeQuery(a, b))


print("-----")


"""
    1st: range frequency counting technique (line sweep) + hashtable
    - similar to lcl094, 1109, 1589, 1854

    e.g. nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]

    idx:0, 1, 2, 3, 4, 5
        1       -1          <- request0
           1       -1       <- request1
           1 -1             <- request2
    ---------------------
        1, 3, 2, 1, 0, 0    <- prefix sum the counts
           ^ here is the result

    Time    O(NlogN)
    Space   O(N)
    3796 ms, faster than 100.00%
"""


class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        counts = n * [0]

        # line sweep
        for s, e in requests:
            counts[s] += 1
            if e + 1 < n:
                counts[e+1] -= 1
        for i in range(1, n):
            counts[i] += counts[i-1]

        nums.sort(reverse=True)
        pq = [(counts[i], i) for i in range(n)]
        pq.sort(reverse=True)

        res = 0
        while len(pq) > 0:
            c, i = pq.pop(0)
            x = nums.pop(0)
            res += x * c
        return res


s = Solution()

a = [1, 2, 3, 4, 5]
b = [[1, 3], [0, 1]]
print(s.maxSumRangeQuery(a, b))

a = [1, 2, 3, 4, 5, 6]
b = [[0, 1]]
print(s.maxSumRangeQuery(a, b))

a = [1, 2, 3, 4, 5, 10]
b = [[0, 2], [1, 3], [1, 1]]
print(s.maxSumRangeQuery(a, b))


print("-----")

"""
    2nd: range count technique

    Time    O(NlogN)
    Space   O(N)
    2124 ms, faster than 100.00%
"""


class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        counts = n * [0]

        # range count techique
        for s, e in requests:
            counts[s] += 1
            if e + 1 < n:
                counts[e+1] -= 1
        for i in range(1, n):
            counts[i] += counts[i-1]

        counts.sort(reverse=True)
        nums.sort(reverse=True)

        res = 0
        for i in range(n):
            res += nums[i] * counts[i]
        return res % (10**9+7)


s = Solution()

a = [1, 2, 3, 4, 5]
b = [[1, 3], [0, 1]]
print(s.maxSumRangeQuery(a, b))

a = [1, 2, 3, 4, 5, 6]
b = [[0, 1]]
print(s.maxSumRangeQuery(a, b))

a = [1, 2, 3, 4, 5, 10]
b = [[0, 2], [1, 3], [1, 1]]
print(s.maxSumRangeQuery(a, b))
