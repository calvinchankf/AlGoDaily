from collections import defaultdict

"""
    1st: 3 hashtables
    - 1 hashtable to store the checkIn info for each (station, person)
    - 1 hashtable to store the total time between (start, end)
    - 1 hashtable to store the total count of travels between (start, end)

    Time    O(1)
    Space   O(3N)
    264 ms, faster than 71.30%
"""


class UndergroundSystem:

    def __init__(self):
        self.ht_checkIns = {}
        self.ht_total = defaultdict(int)
        self.ht_total_count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ht_checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.ht_checkIns[id]
        diff = t - startTime
        self.ht_total[(startStation, stationName)] += diff
        self.ht_total_count[(startStation, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.ht_total[(startStation, endStation)]
        count = self.ht_total_count[(startStation, endStation)]
        return t/count
