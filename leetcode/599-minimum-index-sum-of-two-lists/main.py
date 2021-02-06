"""
    1st: hashtable

    Time    O(S+T)
    Space   O(S)
    144ms beats 90.65%
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ht = {}
        for i in range(len(list2)):
            s = list2[i]
            ht[s] = i
        leastIndexSum = 2**32
        res = []
        for i in range(len(list1)):
            s = list1[i]
            if s in ht:
                indexSum = i + ht[s]
                if indexSum < leastIndexSum:
                    leastIndexSum = indexSum
                    res = [s]
                elif indexSum == leastIndexSum:
                    res.append(s)
        return res
