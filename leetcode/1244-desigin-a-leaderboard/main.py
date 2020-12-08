from collections import defaultdict
from collections import Counter

"""
    1st: binary search + hashtable

    Time of addScore()      O(k), it can be O(logN) depends on language becos of array.insert()
    Time of top()           O(k)
    Time of reset()         O(N) binary search + linear search
    Space                   O(2N)
    44 ms, faster than 87.86%
"""


class Leaderboard(object):

    def __init__(self):
        self.arr = []   # [id0, id1, id2...]
        self.ht = {}    # {id0: score0, id1: score1....}

    def addScore(self, playerId, score):
        newScore = 0
        if playerId in self.ht:
            newScore = self.ht[playerId] + score
            self.ht[playerId] = newScore
            # remove
            i = self.arr.index(playerId)
            self.arr.pop(i)
        else:
            self.ht[playerId] = score
            newScore = score
        # add
        j = self._upperBsearch(self.arr, self.ht, newScore)
        self.arr.insert(j, playerId)

    def top(self, K):
        res = 0
        n = len(self.arr)
        leftBound = max(n-K-1, -1)
        for i in range(n-1, leftBound, -1):
            pId = self.arr[i]
            res += self.ht[pId]
        return res

    def reset(self, playerId):
        i = self.arr.index(playerId)
        self.arr.pop(i)
        del self.ht[playerId]

    def _upperBsearch(self, arr, ht, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            pId = arr[mid]
            if target >= ht[pId]:
                left = mid + 1
            else:
                right = mid
        return right


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


"""
    2nd: just use a hashtable

    ref:
    - https://leetcode.com/problems/design-a-leaderboard/discuss/418866/Python-Counter-1-line-Each

    Time of addScore()      O(1)
    Time of top()           O(N) -> O(NlogK)
    Time of reset()         O(1)
    Space                   O(1)
    112 ms, faster than 23.24%
"""


class Leaderboard(object):

    def __init__(self):
        self.A = Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i, v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0
