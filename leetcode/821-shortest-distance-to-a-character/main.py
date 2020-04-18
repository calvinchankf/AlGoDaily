"""
    1st approach: binary search

    e.g. S = "loveleetcode", C = 'e'

    loveleetcode
       ^ ^^    ^
       3 56    11
    
    for i = 0, closest index is 3, diff = 3-0=3
    for i = 1, closest index is 3, diff = 3-1=2
    for i = 2, closest index is 3, diff = 3-2=1
    for i = 3, closest index is 3, diff = 3-3=0
    ....

    Time    O(nlogn)
    Space   O(n)
    32 ms, faster than 79.41%
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indeces = []
        for i in range(len(S)):
            if S[i] == C:
                indeces.append(i)
        res = []
        for i in range(len(S)):
            idx = self.bsearch(indeces, i)
            res.append(abs(indeces[idx] - i))
        return res

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # checking
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target-nums[left]) < abs(target-nums[right]):
            return left
        return right


"""
    2nd approach: loop forward and backward

    e.g. S = "loveleetcoded", C = 'e'

    l o v e l e e t c o d e d
    * * * 0 1 0 0 1 2 3 4 0 1 <- nearest diff when we go forward
    3 2 1 0 1 0 0 4 3 2 1 0 * <- nearest diff when we go backward

    3,2,1,0,1,0,0,1,2,2,1,0,1 <- min of forward[i] and backward[i]

    Time    O(3n)
    Space   O(2n)
    32 ms, faster than 79.41%
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        forward = []
        prevCIdx = -sys.maxsize
        for i in range(len(S)):
            if S[i] == C:
                prevCIdx = i
            forward.append(i-prevCIdx)

        backward = []
        prevCIdx = sys.maxsize
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prevCIdx = i
            backward.append(prevCIdx-i)
        backward = backward[::-1]

        res = len(S) * [0]
        for i in range(len(S)):
            res[i] = min(forward[i], backward[i])
        return res
