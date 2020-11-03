from collections import defaultdict

"""
    1st: hashtable + sort + 2 pointers

    Time    O(NlogM) N: no. of keyName, M: no. of timestamps a person has on average
    Space   O(N)
    744 ms, faster than 100.00%
"""
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ht = defaultdict(list)
        n = len(keyName)
        for i in range(n):
            t = self.getTime(keyTime[i])
            ht[keyName[i]].append(t)
        res = []
        for p in ht:
            j = 0
            times = sorted(ht[p])
            for i in range(len(times)):
                while times[j] + 60 < times[i]:
                    j += 1
                if i - j + 1 >= 3:
                    res.append(p)
                    break
        return sorted(res)
    
    def getTime(self, s):
        h, m = s.split(':')
        h = int(h)
        m = int(m)
        return h * 60 + m