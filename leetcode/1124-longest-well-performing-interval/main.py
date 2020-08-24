"""
    1st: hashtable
    
    - similar tp k-sum subarray problem
    - create a new array of +1/-1s corresponding to if hours[i] is > 8 or not
    - there are 2 cases when we iterate the polar array
        - if the pfs > 0, it means the longest subarray is the array from index 0 to i
        - if the "pfs - 1" is in the hashtable, it means that from index ht[pfs-1] to i, the sum = 1 which is longest
    - we only save the first occurence of a pfs so to ensure that we can form a longest subarray

    generic approach
    - this question is fucking similar to leetcode 325, 523, 525, 560, 930, 1171
    - find loops <==============================================================
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
        - if currentSum - target in the hastable, the result+1

    ref:
    - https://www.youtube.com/watch?v=H76XMJmBfP0
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(5n)
    Space   O(n)
"""


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        # new array of +1/-1s indicating hours[i] is > 8 or not
        vectors = []
        for h in hours:
            if h > 8:
                vectors.append(1)
            else:
                vectors.append(-1)
        # k-sum subarray
        ht = {}
        pfs = 0
        ans = 0
        for i in range(len(vectors)):
            pfs += vectors[i]
            # if the pfs > 0, it means the longest subarray is the array from index 0 to i
            if pfs > 0:
                ans = i+1
            # if the "pfs - 1" is in the hashtable, it means that from index ht[pfs-1] to i, the subarray is longest
            if pfs-1 in ht:
                ans = max(ans, i - ht[pfs-1])
            # we only save the first occurence of a pfs
            if pfs not in ht:
                ht[pfs] = i
        return ans
