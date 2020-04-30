import heapq

"""
    1st: hashtable + heap
    - intervals problem similar to lc253

    Time    O(NlogN)
    Space   O(N)
    1260 ms, faster than 100.00%
"""


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        ht = {
            'c': [],
            'cr': [],
            'cro': [],
            'croa': [],
            'croak': [],
        }
        prevOf = {
            'r': 'c',
            'o': 'cr',
            'a': 'cro',
            'k': 'croa',
        }
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if c == 'c':
                ht[c].append([i, i + 1])
            else:
                prevPattern = prevOf[c]
                if len(ht[prevPattern]) > 0:
                    start, end = ht[prevPattern].pop(0)
                    nextPattern = prevPattern + c
                    ht[nextPattern].append([start, i + 1])
                else:
                    return -1
        if len(ht['c']) > 0 or len(ht['cr']) > 0 or len(ht['cro']) > 0 or len(ht['croa']) > 0:
            return -1

        intvs = ht['croak']

        # # the above gurantees that the intervals are sorted
        # def cptr(a, b):
        #     if a[0] == b[0]:
        #         return a[1]-b[1]
        #     return a[0]-b[0]
        # intvs = sorted(intvs, cmp=cptr)

        pq = []
        for i in range(len(intvs)):
            start, end = intvs[i]
            if len(pq) > 0 and start >= pq[0]:
                heapq.heapreplace(pq, end)
            else:
                heapq.heappush(pq, end)
        return len(pq)


s = Solution()

print(s.minNumberOfFrogs('croakcroak'))
print(s.minNumberOfFrogs('crcoakroak'))
print(s.minNumberOfFrogs('croakcrook'))
print(s.minNumberOfFrogs('croakcroa'))
