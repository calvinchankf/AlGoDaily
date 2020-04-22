"""
    1st: bit op
    
    /2:  x >>= 1
    +1:  flip all the 1 from the right until we meet 0
        e.g.
            100111 (39)
                +1
            -----------
            101000 (40)
    
    Time     O(NlogN)
    Space    O(N)
    32 ms, faster than 55.89%
"""


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [int(c) for c in s]
        steps = 0
        while len(arr) > 1:
            if arr[-1] == 0:
                arr.pop()
            else:
                ifBreak = False
                for i in range(len(arr)-1, -1, -1):
                    if arr[i] == 1:
                        arr[i] = 0
                    else:
                        arr[i] = 1
                        ifBreak = True
                        break
                if ifBreak == False:
                    arr = [1] + arr
            steps += 1
        return steps
