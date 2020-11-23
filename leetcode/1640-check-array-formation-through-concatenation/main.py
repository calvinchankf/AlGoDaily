"""
    1st: 2 pointers

    Time    O(AP)
    Space   O(1)
    28 ms, faster than 85.03%
"""
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        i = 0
        while i < len(arr):
            
            targetPiece = None
            for p in pieces:
                if p[0] == arr[i]:
                    targetPiece = p
                    break
            if targetPiece == None:
                return False
            
            j = 0
            while j < len(targetPiece):
                if targetPiece[j] == arr[i]:
                    i += 1
                    j += 1
                else:
                    return False
                    
        return True