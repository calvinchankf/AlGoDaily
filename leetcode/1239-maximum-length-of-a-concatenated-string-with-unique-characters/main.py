"""
    1st: recursion
    - in each recursion, we compare the combined string with out temporary result
    - keep track of the characters we have in each recursion
    - only proceed the recursion forward when there are no duplicate characters

    Time    O(2^N)
    Space   O(2^N)
    112 ms, faster than 48.58%
"""


class Solution(object):

    def __init__(self):
        self.s = ''

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.dfs(arr, '', 26*[0])
        return len(self.s)

    def dfs(self, arr, s, counts):
        if len(s) > len(self.s):
            self.s = s
        if len(arr) == 0:
            return
        for i in range(len(arr)):
            cand = arr[i]
            nextCounts = counts[:]
            shouldSkip = False
            for c in cand:
                cIdx = ord(c) - ord('a')
                nextCounts[cIdx] += 1
                if nextCounts[cIdx] > 1:
                    shouldSkip = True
                    break
            if shouldSkip:
                continue
            self.dfs(arr[i+1:], s+cand, nextCounts)


"""
    2nd: recursion
    - same as 1st
    - optimize the speed by passing a starting index when we proceed recursion forward

    Time    O(2^N)
    Space   O(2^N)
    96 ms, faster than 59.43%
"""


class Solution(object):

    def __init__(self):
        self.s = ''

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.dfs(arr, '', 0, 26*[0])
        return len(self.s)

    def dfs(self, arr, s, start, counts):
        if len(s) > len(self.s):
            self.s = s
        if start == len(arr):
            return
        for i in range(start, len(arr)):
            cand = arr[i]
            nextCounts = counts[:]
            shouldSkip = False
            for c in cand:
                cIdx = ord(c) - ord('a')
                nextCounts[cIdx] += 1
                if nextCounts[cIdx] > 1:
                    shouldSkip = True
                    break
            if shouldSkip:
                continue
            self.dfs(arr, s+cand, i+1, nextCounts)
