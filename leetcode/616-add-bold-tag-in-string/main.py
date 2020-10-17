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
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intervals = []
        for word in set(dict):
            t = s.find(word)
            while t > -1:
                intervals.append([t, t+len(word)])  # [start, end)
                t = s.find(word, t+1)
        # sort the intervals, O(nlogn)
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 0:
            return s
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
        for i in range(len(s)+1):
            if i == cur[0]:
                res += '<b>'
            if i == cur[1]:
                res += '</b>'
                if len(merged) > 0:
                    cur = merged.pop(0)
            if i < len(s):
                res += s[i]
        return res
