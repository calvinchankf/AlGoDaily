import sys
from collections import defaultdict

"""
    1st: prefix sum + hashtable + minmax
    - prerequisite: lc560, 915
    - no negative numbers, so the prefixsum is monotonic increasing

    e.g.        [1, 1, 3, 1, 5, 1, 2, 1]
    prefixs ->  [*, *, 2, 2, *, *, *, 3] store the length of subarrays sum to k when we go forward
    prefixs ->  [*, *, 2, 2, 2, 2, 2, 2] store the min length of subarrays when we go forward

    suffixs <-  [*, 2, 2, *, *, 3, *, *] store the length of subarrays sum to k when we go backward
    suffixs <-  [2, 2, 2, 3, 3, 3, *, *] store the min length of subarrays when we go backward

    - Since we only find 2 subarrays, result must be one from left and another from the right
    i.e. res = min(res, prefixs[i] + suffixs[i+1])

    Time    O(5N)
    Space   O(N)
    1964 ms, faster than 11.41%
"""


class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)

        prefixs = n * [sys.maxsize]
        ht = defaultdict(int)
        pfs = 0
        for i in range(n):
            pfs += arr[i]
            if pfs == target:
                prefixs[i] = i + 1
            remain = pfs - target
            if remain in ht:
                prefixs[i] = i - ht[remain]
            ht[pfs] = i

        # print(prefixs)
        for i in range(1, n):
            prefixs[i] = min(prefixs[i-1], prefixs[i])
        # print(prefixs)

        suffixs = n * [sys.maxsize]
        ht = defaultdict(int)
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += arr[i]
            if sfs == target:
                suffixs[i] = n - i
            remain = sfs - target
            if remain in ht:
                suffixs[i] = ht[remain] - i
            ht[sfs] = i

        # print(suffixs)
        for i in range(n-2, -1, -1):
            suffixs[i] = min(suffixs[i], suffixs[i+1])
        # print(suffixs)

        res = sys.maxsize
        for i in range(n-1):
            res = min(res, prefixs[i] + suffixs[i+1])

        if res == sys.maxsize:
            return -1
        return res


s = Solution()

a = [3, 2, 2, 4, 3]
b = 3
print(s.minSumOfLengths(a, b))

a = [7, 3, 4, 7]
b = 7
print(s.minSumOfLengths(a, b))

a = [4, 3, 2, 6, 2, 3, 4]
b = 6
print(s.minSumOfLengths(a, b))

a = [5, 5, 4, 4, 5]
b = 3
print(s.minSumOfLengths(a, b))

a = [3, 1, 1, 1, 5, 1, 2, 1]
b = 3
print(s.minSumOfLengths(a, b))

a = [1, 1, 3, 1, 5, 1, 2, 1]
b = 4
print(s.minSumOfLengths(a, b))

print("-----")

"""
    2nd: same as 1st
    - but compute the final prefixs[] and suffixs[] along the way

    Time    O(3N)
    Space   O(N)
    1752 ms, faster than 16.11%
"""


class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)

        prefixs = n * [sys.maxsize]
        ht = defaultdict(int)
        pfs = 0
        for i in range(n):
            pfs += arr[i]
            if pfs == target:
                prefixs[i] = i + 1
            remain = pfs - target
            if remain in ht:
                prefixs[i] = i - ht[remain]
            ht[pfs] = i
            if i > 0:
                prefixs[i] = min(prefixs[i-1], prefixs[i])
        # print(prefixs)

        suffixs = n * [sys.maxsize]
        ht = defaultdict(int)
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += arr[i]
            if sfs == target:
                suffixs[i] = n - i
            remain = sfs - target
            if remain in ht:
                suffixs[i] = ht[remain] - i
            ht[sfs] = i
            if i < n-1:
                suffixs[i] = min(suffixs[i], suffixs[i+1])
        # print(suffixs)

        res = sys.maxsize
        for i in range(n-1):
            temp = prefixs[i] + suffixs[i+1]
            res = min(res, temp)

        if res == sys.maxsize:
            return -1
        return res


s = Solution()

a = [3, 2, 2, 4, 3]
b = 3
print(s.minSumOfLengths(a, b))

a = [7, 3, 4, 7]
b = 7
print(s.minSumOfLengths(a, b))

a = [4, 3, 2, 6, 2, 3, 4]
b = 6
print(s.minSumOfLengths(a, b))

a = [5, 5, 4, 4, 5]
b = 3
print(s.minSumOfLengths(a, b))

a = [3, 1, 1, 1, 5, 1, 2, 1]
b = 3
print(s.minSumOfLengths(a, b))

a = [3, 1, 1, 1, 5, 1, 2, 1]
b = 4
print(s.minSumOfLengths(a, b))
