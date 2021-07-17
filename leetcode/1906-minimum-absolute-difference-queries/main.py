"""
    1st: hashtable?
    - since the range of numbers is small, we can make a snapshot of frequencies at every index
    e.g. [1,3,4,8]
    start= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
    idx0 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, ...]
    idx1 = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, ...]
    idx2 = [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, ...]
    idx3 = [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, ...]

    then for every query, we can just get the snapshot of frequencies by snapshots[j] - snapshots[i-1]

    Time    O(N + 100Q)
    Space   O(100N)
    3976 ms, faster than 54.46%
"""


class Solution(object):
    def minDifference(self, nums, queries):
        RANGE = 101
        n = len(nums)
        snapshots = [
            RANGE*[0]
        ]
        for i in range(n):
            x = nums[i]
            clone = snapshots[-1][:]
            clone[x] += 1
            snapshots.append(clone)
        # print(snapshots)
        res = []
        for s, e in queries:
            snapshotStart = snapshots[s]
            snapshotEnd = snapshots[e+1]
            snapshot = []
            for i in range(RANGE):
                snapshot.append(snapshotEnd[i] - snapshotStart[i])
            # print(snapshot)
            minDiff = 2**32
            lastAppeared = None
            for i in range(RANGE):
                if snapshot[i] > 0:
                    if lastAppeared:
                        minDiff = min(minDiff, i - lastAppeared)
                    lastAppeared = i
            if minDiff == 2**32:
                res.append(-1)
            else:
                res.append(minDiff)
        return res
