"""
    1st approach: merge intervals
    - similar to lc56, 452, 616, 758
    1. find the positions for the bold tags, [start, end)
	2. sort the intervals, O(nlogn)
	3. merge the intervals
	4. construct result by dequeuing the merged intervels from the front

    Time    O(nlogn)
    Space   O(n)
    36 ms, faster than 89.92%
"""


class Solution(object):
    def boldWords(self, words, S):
        """
        32 ms, faster than 94.95%
        """
        # find the positions for the bold tags
        intervals = []
        for word in set(words):
            t = S.find(word)
            while t > -1:
                # include left, exclude right => [start, end)
                intervals.append([t, t+len(word)])
                t = S.find(word, t+1)
        # sort the intervals, O(nlogn)
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 0:
            return S
        # merge the intervals
        merged = [intervals[0]]
        for interval in intervals:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        # construct result by dequeuing the merged intervels from the front
        res = ""
        cur = merged.pop(0)
        for i in range(len(S)+1):
            if i == cur[0]:
                res += '<b>'
            if i == cur[1]:
                res += '</b>'
                if len(merged) > 0:
                    cur = merged.pop(0)
            if i < len(S):
                res += S[i]

        return res


a = ["ab", "bc"]
b = "aabcd"
# a<b>abc</b>d
print(Solution().boldWords(a, b))

a = ["ab", "cd"]
b = "aabcd"
# a<b>abcd</b>
print(Solution().boldWords(a, b))

a = ["ccb", "b", "d", "cba", "dc"]
b = "eeaadadadc"
# "eeaa<b>d</b>a<b>d</b>a<b>dc</b>"
print(Solution().boldWords(a, b))

a = ["ae", "a", "a", "a", "e"]
b = "cdccccbaab"
# "cdccccb<b>aa</b>b"
print(Solution().boldWords(a, b))

a = ["e", "ad", "ce", "a", "b"]
b = "adcaddeced"
# "<b>ad</b>c<b>ad</b>d<b>ece</b>d"
print(Solution().boldWords(a, b))

a = ["ccb", "a", "cc", "dc", "d"]
b = "bacdcbcced"
# "b<b>a</b>c<b>dc</b>b<b>cc</b>e<b>d</b>"
print(Solution().boldWords(a, b))

# I think Leetcode is incorrect
a = ["e", "cab", "de", "cc", "db"]
b = "cbccceeead"
# "cb<b>ccceee</b>ad"
print(Solution().boldWords(a, b))
