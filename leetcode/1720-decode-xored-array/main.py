"""
    1st: bit op
    - here is the fact we should know:
        A^B = C
    =>  B^C = A 
    =>  A^C = B

    e.g.
        1 0 1 1
    ^   1 1 1 1
    -----------
        0 1 0 0

    Time    O(N)
    Space   O(N)
    228 ms, faster than 84.12%
"""


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(res[-1] ^ i)
        return res
