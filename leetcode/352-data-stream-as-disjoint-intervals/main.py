"""
    1st approach: binary search
    - 

    Time of addNum()            O(n) binary search O(logn) but array.insert() takes O(n)
    Time of getIntervals()      O(1)
    Space                       O(n)
    128 ms, faster than 97.01%
"""


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intvs = []

    def _upperBSearch(self, target):
        arr = self.intvs
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            if target >= arr[mid][1]:
                left = mid + 1
            else:
                right = mid
        return left

    def _extendPrevAndPopCur(self, idx):
        # extend forward and pop curIdx
        prevIdx = idx-1
        if prevIdx >= 0:
            if self.intvs[prevIdx][1] + 1 == self.intvs[idx][0]:
                self.intvs[prevIdx][1] = self.intvs[idx][1]
                self.intvs.pop(idx)

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        idx = self._upperBSearch(val)
        if idx == len(self.intvs):
            # check if intvs[prevIdx] == val
            prevIdx = idx-1
            if prevIdx >= 0 and self.intvs[prevIdx][1] == val:
                return
            self.intvs.append([val, val])
            self._extendPrevAndPopCur(idx)
        else:
            if val+1 == self.intvs[idx][0]:
                # extend the current start
                self.intvs[idx][0] = val
                # if needed, extend forward and pop curIdx, e.g. [0,1] [2,3] => [0,3]
                self._extendPrevAndPopCur(idx)
            elif idx-1 >= 0 and val-1 == self.intvs[idx-1][1]:
                # if needed, extend prev end
                self.intvs[idx-1][1] = val
            elif idx-1 >= 0 and val-1 > self.intvs[idx-1][1] and val+1 < self.intvs[idx][0]:
                # if prev end < val-1 and val+1 < cur start, insert
                self.intvs.insert(idx, [val, val])
            elif idx == 0 and val+1 < self.intvs[idx][0]:
                # if cur == 0 and val+1 < cur start, insert
                self.intvs.insert(idx, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intvs


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

"""
    2nd: sort + hashtable
    - similar to lc128, algoexpert largestRange

    Time of addNum()            O(1)
    Time if getIntervals()      O(N + AlogA)
    2608 ms, faster than 5.12%
"""


class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, val: int) -> None:
        self.nums.append(val)

    def getIntervals(self) -> List[List[int]]:
        n = len(self.nums)
        res = []
        hs = set(self.nums)
        seen = set()
        for i in range(n):
            x = self.nums[i]

            # use a hashset to de-duplicate
            if x in seen:
                continue
            seen.add(x)

            # expand from center to find out the largest consecutive sequence
            left = x
            while left - 1 in hs:
                left -= 1
                seen.add(left)

            right = x
            while right + 1 in hs:
                right += 1
                seen.add(right)

            res.append([left, right])
        return sorted(res)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
