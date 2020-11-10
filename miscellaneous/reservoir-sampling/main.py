import random
"""
    http://www.cse.cuhk.edu.hk/~taoyf/course/5705f10/lec7.pdf

    Question: Given a set S of items, compute a random sample set of size k

    Approach: Reservoir Sampling
    e.g. [59, 100, 2, 30, 63,...]
    - The first k items are directly added to the sampleset. So sampleset = [59, 100, 2]
    - Given the 4th item, the algorithm generates a random integer x from 1 to 4. 
        Assume that the generated x = 4. As x > k, this item is ignored.
    - Given the 5th item, again, the algorithm generates x randomly, 
        but now from 1 to 5. Assume that x = 2 this time. 
        Hence, the item is added to samples, and replaces the 2nd value there. 
        Hence, samples becomes [59, 63, 2].
    - The remaining items are processed in the same manner

    Proof: the calculation of probability of any one of the items
    = Selected * NotSelected * NotSelected * NotSelected..... * NotSelected
    = T * F * F * ... * F
    = 1/i * (1-1/(i+1)) * (1-1/(i+2)) * ... * (1 - 1/n)
    = 1/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n
    = 1/n

    lets say when i = 1,
    = 1/1 *   1/2   *     2/3     * ... * (n-1)/n
    = 1/n
"""

"""
    Approach for an array
"""


def reservoirSampling(nums, k):
    sampleSet = []
    for i in range(len(nums)):
        x = nums[i]
        if i < k:
            sampleSet.append(x)
        else:
            r = random.randint(0, i)
            if r < k:
                sampleSet[r] = x
    return sampleSet


a = [59, 100, 2, 30, 63, 71, 12, 25, 86, 48]
b = 3
print(reservoirSampling(a, 3))

print("-----")

"""
    Approach for a Data Stream
"""


class ReservoirSampling(object):
    def __init__(self, k=1):
        self.sampleSet = []
        self.k = k
        self.idx = 0

    def add(self, item):
        if len(self.sampleSet) < self.k:
            self.sampleSet.append(item)
        else:
            r = random.randint(0, self.idx)
            if r < self.k:
                self.sampleSet[r] = item
        self.idx += 1

    def getSampleSet(self):
        return self.sampleSet

    def addAndGet(self, item):
        self.add(item)
        return self.getSampleSet()


rs = ReservoirSampling(3)
print(rs.addAndGet(59))
print(rs.addAndGet(100))
print(rs.addAndGet(2))
print(rs.addAndGet(30))
print(rs.addAndGet(63))
print(rs.addAndGet(71))
print(rs.addAndGet(12))
print(rs.addAndGet(25))
print(rs.addAndGet(86))
print(rs.addAndGet(48))
