"""
    1: bitop + hashtable
    - computing xor prefixes at every index
    
    e.g. 1
    3   = 00011 
    10  = 01010
    5   = 00101
    25  = 11001
    2   = 00010
    8   = 01000

    XOR at index:
    at index 0: we want to find 10000
        result: 25 ^ other numbers
    at index 1: we want to find 11000 
        result: 25 ^ 2, 25 ^ 3, 25 ^ 5
    at index 2: we want to find 11100
        result: 25 ^ 5 = 
    at index 2: we want to find 11110
        no result
    at index 3: we want to find 11101
        no result
    
    so the final result is 25 ^ 5 = 28 

    e.g. 5
    5 = 0101
    8 = 1000
    
    XOR at index:
    at index 0: we want to find 1000
        result: 5 ^ 8
    at index 1: we want to find 1100
        result: 5 ^ 8
    at index 2: we want to find 1110
        no result
    at index 3: we want to find 1101
        no result
    so the final result is 5 ^ 8


    Time    O(NlogN)
    Space   O(N)
    136 ms, faster than 60.46%
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        maxLength = len(format(maxNum, 'b'))
        res = 0
        # loop from leftost to rightmost
        for i in range(maxLength-1, -1, -1):
            # go to the next bit by the left shift
            res <<= 1
            # set 1 in the smallest bit
            curr_xor = res | 1
            # compute all existing prefixes
            prefixes = set()
            for num in nums:
                prefixes.add(num >> i)
            # Update res, if two of these prefixes could result in curr_xor
            b = False
            for p in prefixes:
                b |= curr_xor ^ p in prefixes
            res |= b

        return res
