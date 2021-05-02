from heapq import *

"""
    1st: 2 heaps
    - the idea is simple, but the implementation is annoying

    Time    O(NlogN)
    Space   O(N)
    832 ms, faster than 100.00%
"""

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        minheapSells = [] # stores sell orders
        maxheapBuys = [] # stores buy orders
        for i in range(len(orders)):
            p, a, t = orders[i]
            if t == 0:
                
                while len(minheapSells) > 0:
                    _p, _a = heappop(minheapSells)
                    if _p <= p:
                        a -= _a
                        if a < 0:
                            heappush(minheapSells, (_p, -a))
                            break
                    else:
                        heappush(minheapSells, (_p, _a))
                        break
                
                if a > 0:
                    heappush(maxheapBuys, (-p, a))
                
            elif t == 1:
                
                while len(maxheapBuys) > 0:
                    _p, _a = heappop(maxheapBuys)
                    _p *= -1 # negative due to the maxheap
                    if _p >= p:
                        a -= _a
                        if a < 0:
                            heappush(maxheapBuys, (-_p, -a))
                            break
                    else:
                        heappush(maxheapBuys, (-_p, _a))
                        break
                
                if a > 0:
                    heappush(minheapSells, (p, a))
        
        res = 0
        for _, a in minheapSells:
            res += a
            res %= 10**9 + 7
        for _, a in maxheapBuys:
            res += a
            res %= 10**9 + 7
        return res