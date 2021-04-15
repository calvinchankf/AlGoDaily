"""
    1st: hashtable
    
    Time    O(N)
    Space   O(N)
    208 ms, faster than 100.00%
"""


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        m = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        res = 0
        for item in items:
            if item[m[ruleKey]] == ruleValue:
                res += 1
        return res
