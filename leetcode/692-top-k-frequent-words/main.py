from collections import defaultdict
from functools import cmp_to_key

"""
    1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys
	3. put the hashtable key&value into a bucket with freq as an index
	4. the first k elements are the top k elements in the bucket

	Time	O(nlogn * klogk)
	Space	O(n)
	44 ms, faster than 67.17%
	30may2019
"""


class Solution(object):
    def topKFrequent(self, words, k):
        ht = defaultdict(int)
        for w in words:
            ht[w] += 1

        arr = []
        for key in ht:
            arr.append((ht[key], key))

        def cmptr(a, b):
            if a[0] == b[0]:
                return -1 if a[1] < b[1] else 1
            return b[0] - a[0]
        arr.sort(key=cmp_to_key(cmptr))

        res = []
        for i in range(min(k, len(arr))):
            res.append(arr[i][1])
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

print("-----")

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
