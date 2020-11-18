import random

"""
    https://leetcode.com/discuss/interview-question/451431/

    Given an array of integers arr, randomly return an index of the maximum value seen by far.

    Example:
    Input: [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]

     0   1   2  3   4   5   6  7  8   9
    [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]

    idx0: 11 is largest, indices are [0]
    idx1: 30 is largest, indices are [1]
    idx2: 30 is largest, indices are [1]
    idx3: 30 is largest, indices are [1,3], pick either one of them
    idx4: 30 is largest, indices are [1,3,4], pick one of them
    idx5: 30 is largest, indices are [1,3,4,5], pick one of them
    idx6: 30 is largest, indices are [1,3,4,5], pick one of them
    idx7: 30 is largest, indices are [1,3,4,5], pick one of them
    idx8: 62 is largest, indices are [8]
    idx9: 62 is largest, indices are [8,9], pick either one of them


    Having iterated up to the at element index 5 (where the last 30 is), randomly give an index among [1, 3, 4, 5] which are indices of 30 - the max value by far. Each index should have a 1/4 chance to get picked.
    Having iterated through the entire array, randomly give an index between 8 and 9 which are indices of the max value 62.
"""


"""
    Reservoir Sampling:
    the calculation of probability of any one of the items
    = Selected * NotSelected * NotSelected * NotSelected..... * NotSelected
    = T * F * F * ... * F
    = 1/i * (1-1/(i+1)) * (1-1/(i+2)) * ... * (1 - 1/n)
    = 1/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n
    = 1/n

    lets say when i = 1,
    = 1/1 *   1/2   *     2/3     * ... * (n-1)/n
    = 1/n
"""


def getRandomIndexOfMaxNumber(nums):
    maxNum = -2**31
    maxIdx = -1
    targetIndexCount = 0
    res = []
    for i in range(len(nums)):
        x = nums[i]
        if x > maxNum:
            maxNum = x
            maxIdx = i
            count = 1
        elif x == maxNum:
            # pick the current number with probability 1 / count (reservoir sampling)
            targetIndexCount += 1
            if random.randint(1, targetIndexCount) == 1:
                maxIdx = i
        res.append(maxIdx)
    return res


a = [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
print(getRandomIndexOfMaxNumber(a))

print("-----")

"""
    followup: data stream
"""


class DataStream(object):

    def __init__(self):
        self.maxNum = -2**31
        self.maxNumIdx = -1
        self.maxNumCount = 0
        self.idx = 0  # we might consider using ID

    def add(self, num):
        if num > self.maxNum:
            self.maxNum = num
            self.maxNumIdx = self.idx
            self.maxNumcount = 1
        elif num == self.maxNum:
            self.maxNumCount += 1
            if random.randint(1, self.maxNumCount) == 1:
                self.maxNumIdx = self.idx
        self.idx += 1  # if we use ID, this function should be add(num, id)

    def getRandomIndexOfMaxNum(self):
        return self.maxNumIdx

    def addAndGet(self, num):
        self.add(num)
        return self.getRandomIndexOfMaxNum()


ds = DataStream()
print(ds.addAndGet(11))     # [0]
print(ds.addAndGet(30))     # [1]
print(ds.addAndGet(2))      # [1]
print(ds.addAndGet(30))     # [1,3]
print(ds.addAndGet(30))     # [1,3,4]
print(ds.addAndGet(30))     # [1,3,4,5]
print(ds.addAndGet(6))      # [1,3,4,5]
print(ds.addAndGet(2))      # [1,3,4,5]
print(ds.addAndGet(62))     # [8]
print(ds.addAndGet(62))     # [8,9]
