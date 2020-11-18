import heapq
from collections import Counter

"""
    1st approach: hashtable + sort
    - count num: freq into a hashtable
    - put the hashtable key&value into a priority queue

    Time    O(NlogN)
    SPace   O(N)
    92 ms, faster than 78.84%
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        freqs = []
        for key in counter:
            f = counter[key]
            freqs.append((f, key))
        freqs.sort(reverse=True)
        res = []
        for f, key in freqs[:k]:
            res.append(key)
        return res


print(Solution().topKFrequent([], 0))
print(Solution().topKFrequent([], 1))
print(Solution().topKFrequent([1], 0))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1], 2))
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent(
    [1, 1, 1, 2, 2, 3, 4, 1, 2, 1, 3, 3, 4, 3], 2))

print("-----")

"""
    2nd approach: hashtable + quick select
    - "You can return the answer in any order" <- because of this, we can use quickselect
    - count num: freq into a hashtable
    - use quick select the arrange the k-1 smallest elements present before kth elements

    48ms beats 34.16%
    21mar2019
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        if k > len(nums):
            return []
        # a list of tuples, for value it is (value, freq)
        counts = list(Counter(nums).items())
        kth = self.kthBiggest(counts, k)
        res = []
        for x in counts[:kth+1]:
            res.append(x[0])
        return res

    def kthBiggest(self, nums, k):
        return self.helper(nums, 0, len(nums)-1, k)

    def helper(self, nums, left, right, k):
        if k > 0 and k <= len(nums):
            pIdx = self.partition(nums, left, right)
            if pIdx+1 == k:
                return pIdx
            elif pIdx+1 < k:
                return self.helper(nums, pIdx+1, right, k)
            else:
                return self.helper(nums, left, pIdx-1, k)
        return -1

    def partition(self, nums, left, right):
        pivot = nums[right][1]
        pIdx = left
        for i in range(left, right):
            # > for descending
            if nums[i][1] >= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[pIdx], nums[right] = nums[right], nums[pIdx]
        return pIdx


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 4, 1, 2, 1, 3, 3, 4, 3], 2))

print("-----")

"""
    3rd approach: bucket sort
    - count occurence of a num and put it into a hashtable, {num: freq} 
    - create buckets with maxfreq
    - pop the first k num with the maxfreq

    Time    O(N)
    Space   O(N)
    84 ms, faster than 75.45%
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        # count occurence of each num
        ht = Counter(nums)
        # create buckets
        minFreq, maxFreq = 2**32, 0
        freqs = defaultdict(list)
        for x in ht:
            f = ht[x]
            freqs[f].append(x)
            minFreq = min(minFreq, f)
            maxFreq = max(maxFreq, f)
        # put k items into the array
        res = []
        for f in range(maxFreq, minFreq-1, -1):
            if f not in freqs:
                continue
            for num in freqs[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
