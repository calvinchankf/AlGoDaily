"""
    1st: array
    - i didnt understand the question, the description is ambiguous
    - i knew whats going on after i watched the reference on youtube
    - find and update the max at every index
    
    ref:
    - https://www.youtube.com/watch?v=twYLu4hEKnQ

    Time    O(N)
    Space   O(1)
    48 ms, faster than 5.30%
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        biggest = 0
        for i in range(len(arr)):
            num = arr[i]
            biggest = max(biggest, num)
            if biggest == i:
                res += 1
        return res
