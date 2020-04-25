import heapq

"""
    1st: max heap
    - basic idea is, lets say A >> B >> C,  add 'aab' to the result
    
    e.g.1
    
    10: A
    2:  B
    1:  C
    res = AAB
    8: A
    1: B
    1: C
    res = AAB + AAB
    6: A
    1: C
    res = AAB + AAB + AAC
    4: A
    res = AAB + AAB + AAC + AA

    e.g.2
    4: A
    4: B
    1: C
    res = AAB
    3: B
    2: A
    1: C
    res = AAB + B
    2: A <- loot at the code when we do heappush, we add A first then B
    2: B
    1: C
    res = AAB + B + AAB
    1: B
    1: C
    res = AAB + B + AAB + BC
"""


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))
        res = ''
        while len(pq) > 0:
            count0, char0 = heapq.heappop(pq)
            count0 = -count0
            if len(res) > 0:
                if res[-1] == res[-2] == char0:
                    break
                elif res[-1] == char0:  # corner case: A=4, B=4, C=3, we will have AAB + B + go on
                    res += char0
                    count0 -= 1
                    if count0 > 0:
                        heapq.heappush(pq, (-count0, char0))
                    continue

            if count0 >= 2:
                res += 2 * char0
                count0 -= 2
            else:
                res += char0
                count0 -= 1

            if len(pq) > 0:
                count1, char1 = heapq.heappop(pq)
                count1 = -count1
                res += char1
                count1 -= 1
                if count1 > 0:
                    heapq.heappush(pq, (-count1, char1))
            if count0 > 0:
                heapq.heappush(pq, (-count0, char0))
        return res


s = Solution()

print(s.longestDiverseString(1, 1, 7))

print(s.longestDiverseString(2, 2, 1))

print(s.longestDiverseString(7, 1, 0))

print(s.longestDiverseString(4, 4, 3))

print(s.longestDiverseString(4, 4, 1))

print(s.longestDiverseString(2, 2, 1))

# test order if draw
pq = []
heapq.heappush(pq, (3, 'A'))
heapq.heappush(pq, (3, 'B'))
heapq.heappush(pq, (3, 'C'))

while len(pq) > 0:
    print(heapq.heappop(pq))
"""
print:
(3, 'A')
(3, 'B')
(3, 'C')
"""
