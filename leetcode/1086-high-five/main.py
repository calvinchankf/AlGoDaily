"""
    1st approach: sort + hashtable
    - sort the scores from high to low so the higher scores come first
    - use hashtable to put the scores to corresponding sids(student id)
    - construct result by iterating the sid from ascendingly

    Time    O(NlogN)
    Space   O(N)
    64 ms, faster than 30.29%
"""


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items = sorted(items, key=lambda x: x[1], reverse=True)
        m = {}
        for sid, score in items:
            if sid not in m:
                m[sid] = [score]
            else:
                if len(m[sid]) < 5:
                    m[sid].append(score)
        sids = []
        for key in m:
            sids.append(key)
        sids = sorted(sids)
        res = []
        for sid in sids:
            res.append([sid, sum(m[sid])//5])
        return res
