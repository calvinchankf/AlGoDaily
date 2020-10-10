import heapq
from collections import Counter

"""
    1st approach: hashtable + sort
    - count num: freq into a hashtable
    - put the hashtable key&value into a priority queue

    92 ms, faster than 78.84%
    3july2019
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        freqs = []
        for num in counter:
            freqs.append((counter[num], num))
        freqs.sort(reverse=True)
        res = []
        for i in range(min(len(freqs), k)):
            res.append(freqs[i][1])
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

    Time    O(n)
    Space   O(n)
    88 ms, faster than 88.59%
    9july2019
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        # count occurence of each num
        maxFreq = 0
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
            # getting the maxFreq
            maxFreq = max(maxFreq, ht[num])
        # create buckets
        occurArr = []
        for _ in range(maxFreq+1):
            occurArr.append([])
        # index of occurArr is the occurence
        for key in ht:
            occurence = ht[key]
            occurArr[occurence].append(key)
        # construct result
        res = []
        count = 0
        # start from num with max freq
        for i in range(len(occurArr)-1, -1, -1):
            arr = occurArr[i]
            for num in arr:
                res.append(num)
                count += 1
                if count == k:
                    # if k <= number of unique nums
                    return res
        # if k > number of unique nums
        return res
