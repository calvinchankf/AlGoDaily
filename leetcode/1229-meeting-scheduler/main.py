"""
    1st: sort
    - meeting room + 2 pointers
    
    Time    O(MlogM + NlogN)
    Space   O(1)
    780 ms, faster than 9.47% ....weird
"""


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            start = max(start1, start2)
            end = min(end1, end2)
            if end - start >= duration:
                return [start, start + duration]
            elif end1 > end2:
                j += 1
            elif end2 > end1:
                i += 1
            else:
                i += 1
                j += 1
        return []
