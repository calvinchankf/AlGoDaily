"""
    1st: string
    - be careful of the corner cases

    case 1:
    '012a012'
    result = 1

    case 2:
    '012a0123'
    result = 2
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen = set()
        num_str = ''
        for c in word:
            if c.isdigit():
                num_str += c
            else:
                if len(num_str) > 0:
                    d = int(num_str)
                    seen.add(d)
                num_str = ''
        if len(num_str) > 0:
            d = int(num_str)
            seen.add(d)
        return len(seen)
