"""
    1st: brute force array checking
    - an array for at least single booked
    - an another array for overlapped times
    - check if there is an overlap every time we book

    Time    O(N^2)
    Space   O(2N)
    756 ms, faster than 36.44%
"""


class MyCalendarTwo:

    def __init__(self):
        self.singles = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.singles:
            if start < e and end > s:
                self.overlaps.append((max(s, start), min(e, end)))
        self.singles.append((start, end))
        return True
