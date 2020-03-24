"""
    1st: prefix sum
    - compute the prefix sum of XOR at each index
    - since x^y^x = y, prefixSums[from-1] ^ prefixSums[right] is what we want for every query

    Time    O(A + Q)
    Space   O(A)
    432 ms, faster than 20.51%
"""


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSums = []
        for i in range(len(arr)):
            num = arr[i]
            if i == 0:
                prefixSums.append(num)
            else:
                prefixSums.append(prefixSums[-1] ^ num)
        res = []
        for left, right in queries:
            temp = prefixSums[right]
            if left > 0:
                temp ^= prefixSums[left-1]
            res.append(temp)
        return res
