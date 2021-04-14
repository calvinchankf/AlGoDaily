"""
    1st: array

    Time    O(N)
    Space   O(N)
"""
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        j = -1
        for i in range(len(s)):
            if s[i] == '1':
                if i != j + 1:
                    return False
                j = i
        return True
