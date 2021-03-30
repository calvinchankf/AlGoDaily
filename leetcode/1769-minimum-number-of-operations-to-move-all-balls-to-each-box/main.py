"""
    1st: math?
    - prefix sum with indices

    Time    O(N)
    Space   O(N)
    60 ms, faster than 100.00%
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftCount = 0
        leftSum = 0
        rightCount = 0
        rightSum = 0
        for i in range(len(boxes)):
            if boxes[i] == '1':
                rightCount += 1
                rightSum += i
        res = []
        for i in range(len(boxes)):
            res.append(leftSum + rightSum)
            if boxes[i] == '1':
                leftCount += 1
                rightCount -= 1
            leftSum += leftCount
            rightSum -= rightCount
        return res
