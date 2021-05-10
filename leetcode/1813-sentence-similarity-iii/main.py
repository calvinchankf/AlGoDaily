"""
    1st: 2 pointers
    - i dont like dealing with indices, so i remove the prefix words and suffix words directly

    28 ms, faster than 89.30%
"""
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        largerArr, smallerArr = [], []
        if len(words1) >= len(words2):
            largerArr, smallerArr = words1, words2
        else:
            largerArr, smallerArr = words2, words1
        
        while len(smallerArr) > 0 and smallerArr[0] == largerArr[0]:
            smallerArr.pop(0)
            largerArr.pop(0)
        
        if len(smallerArr) == 0:
            return True
        
        while len(smallerArr) > 0 and smallerArr[-1] == largerArr[-1]:
            smallerArr.pop()
            largerArr.pop()
        
        return len(smallerArr) == 0