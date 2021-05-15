"""
    1st: hashtable

    Time    O(N)
    Space   O(26)
    16 ms, faster than 92.05%
"""
class Solution(object):
    def checkIfPangram(self, sentence):
        counts = 26 * [0]
        for c in sentence:
            i = ord(c) - ord('a')
            counts[i] += 1
        for c in counts:
            if c == 0:
                return False
        return True