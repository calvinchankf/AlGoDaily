from collections import *

"""
    1st approach:
    - use oredered dict
    - put all the keys into the ordered dict
    - find the farthest reach of deletion
    - for each character, decrement the count in the ordereddict
    - check if the occurence in the front of the current char are all zeros

    Time    O(n^2)
    Space   O(n)
    348 ms, faster than 5.04%
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # put all the keys into the ordered dict
        od = OrderedDict()
        for c in S:
            if c in od:
                od[c] += 1
            else:
                od[c] = 1

        res = []
        # for finding the farthest reach of deletion
        farthestReachCountInOd = 0
        deleteCount = 0
        # for each character, decrement the count in the ordereddict
        for c in S:
            od[c] -= 1
            deleteCount += 1
            curIdx = od.keys().index(c)  # idx of current character in ordereddict
            items = od.items()
            farthestReachCountInOd = max(farthestReachCountInOd, curIdx)

            if od[c] == 0:
                isAllZerosFromFront = True
                # in ordereddict,
                # check if the occurence in the front of the current char are all zeros
                for i in range(farthestReachCountInOd, -1, -1):
                    key, cnt = items[i]
                    if cnt > 0:
                        isAllZerosFromFront = False
                        break
                # if yes, do partition
                if isAllZerosFromFront == True:
                    res.append(deleteCount)
                    deleteCount = 0
                    farthestReachCountInOd = 0
                    for i in range(farthestReachCountInOd, -1, -1):
                        key, cnt = items[i]
                        del od[key]
        return res


print(Solution().partitionLabels("abccaddbeffe"))

"""
    2nd approach:
    - simplify and optimze the 1st approach
    - we can just save the char: last index in the hashtable
    - find the farthest reach of deletion during iteration
    - once i == farthest reach, the substring between i and previous end(this start point) is the result

    Time    O(n)
    Space   O(n)
    28 ms, faster than 93.82%
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # put all the keys into the ordered dict
        m = {}
        for i in range(len(S)):
            c = S[i]
            m[c] = i
        res = []
        # for finding the farthest reach
        farthest = -1
        # for recording the substring start point
        startPoint = -1
        # iterate the string to record the farthest point a substring can reach
        for i in range(len(S)):
            c = S[i]
            farthest = max(farthest, m[c])
            # check if the farthest == i. if yes, it means the substring btw startpoint and i is one of the result
            if i == farthest:
                res.append(farthest-startPoint)
                startPoint = i
        return res


print(Solution().partitionLabels("abccaddbeffe"))
