"""
    1st approach: 2 pointers
    - exactly the same question lc159
    - maintain the sliding window to have 2 unique keys
    
    The question is so confusing, lets rephrase the quesion:
    Given a string, find the max length of a substring which has only 2 distinct characters
	e.g. "ababacddc", return 5
	becos length of "ababa" = 5, where all other substrings are < 5
	e.g.
	length of "abab" = 4
	length of "cddc" = 4
	.
    .
    .

    Time    O(n)
    Space   O(n)
    768 ms, faster than 20.82%
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        res = 0
        slow = 0
        ht = {}
        for i in range(len(tree)):
            fruit = tree[i]
            if fruit not in ht:
                ht[fruit] = 1
            else:
                ht[fruit] += 1
            # maintain the sliding window to have 2 unique keys
            while len(ht) > 2:
                last = tree[slow]
                ht[last] -= 1
                slow += 1  # move slow forward
                if ht[last] == 0:
                    del ht[last]
            res = max(res, i-slow+1)
        return res
