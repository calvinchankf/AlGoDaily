# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

"""
    1st: array
    - bad description
    - in short, lets say we want to read the first 5 characters from "leetcode" using read4()

    1. when we call read4(interanlBuffer), interanlBuffer = [l, e, e, t]
    so then we push all 4 items from interanlBuffer to our result by buf.push()

    2. when we call read4(interanlBuffer), interanlBuffer = [c, o, d, e]
    since we only need 1 more character, we only have to push the "c" into buff

    As a result,
    interanlBuffer = [o, d, e]
    buff = [l, e, e, t, c]

    Time    O(N)
    Space   O(4)
    20 ms, faster than 99.15%
"""
class Solution:
    
    def __init__(self):
        self.buf4 = []
    
    def read(self, buf: List[str], n: int) -> int:
        total = 0
        while total < n:
            if len(self.buf4) == 0:
                buf4 = 4 * ['']
                c = read4(buf4)
                if c == 0:
                    break
                self.buf4 = buf4[:c]
            while total < n and len(self.buf4) > 0:
                top = self.buf4.pop(0)
                buf[total] = top
                total += 1
        return total