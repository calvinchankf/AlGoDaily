class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hs = set()
        for x in arr:
            hs.add(x)
        res = 0
        for x in arr:
            if x + 1 in hs:
                res += 1
        return res
