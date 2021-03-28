"""
    1st: backtracking

    Time    less than O(N^N)
    Space   O(N)
    40 ms, faster than 52.00%
"""


class Solution(object):
    def constructDistancedSequence(self, n):
        seq = (2*n - 1) * [None]
        unused = set([x for x in range(1, n+1)])
        self.backtracking(n, seq, unused)
        return seq

    def backtracking(self, n, seq, unused):
        if len(unused) == 0:
            return True
        # find the vaccancy
        j = -1
        for i in range(len(seq)):
            if seq[i] == None:
                j = i
                break
        if j == -1:
            return False
        # try every unused, in descending order for lexicography
        for x in sorted(list(unused), reverse=True):

            if x == 1:
                # select
                seq[j] = x
                unused.remove(x)
                # explore
                if self.backtracking(n, seq, unused):
                    return True
                # backtrack
                seq[j] = None
                unused.add(x)
            else:
                if j+x >= len(seq):
                    continue
                if seq[j] != None or seq[j+x] != None:
                    continue
                # select
                seq[j] = x
                seq[j+x] = x
                unused.remove(x)
                # explore
                if self.backtracking(n, seq, unused):
                    return True
                # backtrack
                seq[j] = None
                seq[j+x] = None
                unused.add(x)
        return False
