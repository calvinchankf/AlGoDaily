"""
    1st: sliding window
    - similar to lc904

    Time    O(2N)
    Space   O(N)
    256 ms, faster than 7.95%
"""


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        res = 0
        curWindow = ''
        curCost = 0
        for i in range(len(s)):

            # add the cost
            curCost += abs(ord(s[i]) - ord(t[i]))
            curWindow += s[i]

            # if the curCost > maxCost,
            # strip out the left most characters one by one until the curCost <= maxCost
            while curCost > maxCost:
                k = len(curWindow)
                curCost -= abs(ord(s[i-k+1]) - ord(t[i-k+1]))
                curWindow = curWindow[1:]

            # update the result if necessary
            res = max(res, len(curWindow))
        return res


"""
    2nd: sliding window
    - same as 1st but maintain a length of curWindow instead

    Time    O(2N)
    Space   O(N)
    256 ms, faster than 7.95%
"""


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        res = 0
        curLen = 0
        curCost = 0
        for i in range(len(s)):

            # add the cost
            curCost += abs(ord(s[i]) - ord(t[i]))
            curLen += 1

            # if the curCost > maxCost,
            # strip out the left most characters one by one until the curCost <= maxCost
            while curCost > maxCost:
                curCost -= abs(ord(s[i-curLen+1]) - ord(t[i-curLen+1]))
                curLen -= 1

            # update the result if necessary
            res = max(res, curLen)
        return res
