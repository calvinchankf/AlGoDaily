from heapq import *
from collections import *
from functools import cmp_to_key

"""
    1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys
	3. put the hashtable key&value into a bucket with freq as an index
	4. the first k elements are the top k elements in the bucket

	Time	O(NlogN)
	Space	O(n)
	44 ms, faster than 67.17%
	30may2019
"""


class Solution(object):
    def topKFrequent(self, words, k):
        ht = Counter(words)
        freqs = []
        for w in ht:
            freqs.append((ht[w], w))
        freqs.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for f, w in freqs[:k]:
            res.append(w)
        return res


a = ["love", "i", "leetcode", "i", "love", "coding"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
b = 4
print(Solution().topKFrequent(a, b))

a = ["aaa", "aa", "a"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["i", "love", "leetcode", "i", "love", "coding"]
b = 3
print(Solution().topKFrequent(a, b))

print("-----")


class WrapString:
    def __init__(self, string):
        self.val = string

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        # goal: desceding order
        return self.val > other.val


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ht = Counter(words)
        minHeap = []
        for w in ht:
            f = ht[w]
            heappush(minHeap, (f, WrapString(w), w))
            if len(minHeap) > k:
                heappop(minHeap)
        res = []
        while len(minHeap) > 0:
            f, o, w = heappop(minHeap)
            res.append(w)
        return res[::-1]


a = ["love", "i", "leetcode", "i", "love", "coding"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
b = 4
print(Solution().topKFrequent(a, b))

a = ["aaa", "aa", "a"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["i", "love", "leetcode", "i", "love", "coding"]
b = 3
print(Solution().topKFrequent(a, b))

"""
    followup: if there is a tie, two words have the same frequency, return them by the insertion order

	Time	O(nlogn * klogk)
	Space	O(n)
	44 ms, faster than 67.17%
	30may2019
"""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = OrderedDict()
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        occurences = {}
        keys = []
        for key in m:
            occurence = m[key]
            if occurence not in occurences:
                keys.append(occurence)
                occurences[occurence] = [key]
            else:
                occurences[occurence].append(key)
        keys = sorted(keys, reverse=True)
        count = 0
        res = []
        for i in range(len(keys)):
            freq = keys[i]
            strings = occurences[freq]
            for s in strings:
                res.append(s)
                count += 1
                if count == k:
                    break
            if count == k:
                break
        return res


a = ["love", "i", "leetcode", "i", "love", "coding"]
b = 2
print(Solution().topKFrequent(a, b))

a = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
b = 4
print(Solution().topKFrequent(a, b))

a = ["aaa", "aa", "a"]
b = 2
print(Solution().topKFrequent(a, b))
