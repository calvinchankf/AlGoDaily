"""
    1st: very annoying math
    - calculate the correct timeslot where startTime and finishTime belong to
    - result = right - left
    - but if left > rigt, split the calculation into 2 days

    Time    O(1)    no iteration, only math
    Space   O(1)
    24 ms, faster than 100.00%
"""


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        left = self.getSlot(self.getHHMM(startTime, 1))
        right = self.getSlot(self.getHHMM(finishTime, -1))
        if left > right:
            a = self.getSlot((23, 59)) - left
            b = right - self.getSlot((0, 0))
            return a + b + 1

        return right - left

    def getHHMM(self, T, d):
        hh = int(T[:2])
        mm = int(T[3:])
        if d == -1:
            return hh, (mm // 15) * 15
        mm = ((mm + 14) // 15) * 15
        if mm == 60:
            return (hh + 1) % 24, 0
        return hh, mm

    def getSlot(self, hhmm):
        hh, mm = hhmm
        return 4 * hh + (mm // 15)
