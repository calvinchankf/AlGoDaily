"""
    https://leetcode.com/discuss/interview-question/614096/Facebook-or-Recruiting-Portal-or-Passing-Yearbooks

    This question is from Facebook recruiting portal.

    There are n students, numbered from 1 to n, each with their own yearbook. 
    They would like to pass their yearbooks around and get them signed by other students.
    You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). 
    The meaning of this list is described below.
    
    Initially, each student is holding their own yearbook. 
    The students will then repeat the following two steps each minute: 
    1. Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), 
    2. and then they'll pass it to student arr[i]. It's possible that arr[i] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
    
    It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
    You must compute a list of n integers output, whose ith element is equal to the number of signatures that will be present in student i's yearbook once they receive it back.*

    Signature
    int[] findSignatureCounts(int[] arr)
    Input
    n is in the range [1, 100,000].
    Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
    Output
    Return a list of n integers output, as described above.

    Example 1
    n = 2
    arr = [2, 1]
    output = [2, 2]
    The first student will sign their own yearbook and pass it to the second, who will also sign it and pass it back to the first student, resulting in 2 signatures. 
    Meanwhile, the second student's yearbook will similarly be signed both by themselves and then by the first student.

    Example 2
    n = 2
    arr = [1, 2]
    output = [1, 1]
    Each student will simply pass their yearbook back to themselves, resulting in 1 signature each.

    Example 3
    n = 5
    arr = [4,3,2,5,1]
    output = [3,2,2,3,3]
    Explanation:
    Person 1: 4 -> 5 -> 1
    Person 2: 3 -> 2
    Person 3: 2 -> 3
    Person 4: 5 -> 1 -> 4
    Person 5: 1 -> 4 -> 5
"""

"""
    1st: brute force
"""


def findSignatureCounts(arr):
    n = len(arr)
    res = []
    for i in range(n):
        k = i
        count = 1
        while arr[k] != i + 1:
            count += 1
            k = arr[k] - 1
        res.append(count)
    return res


a = [1, 2]
print(findSignatureCounts(a))

a = [2, 1]
print(findSignatureCounts(a))

a = [4, 3, 2, 5, 1]
print(findSignatureCounts(a))

a = [5, 1, 2, 3, 6, 4]
print(findSignatureCounts(a))

print("-----")

"""
    2nd: union find
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.roots = {}
        self.caps = {}
        for i in range(n):
            self.roots[i] = i
            self.caps[i] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


def findSignatureCounts(arr):
    nums = [x - 1 for x in arr]
    n = len(nums)
    uf = UnionFind(n)
    for i in range(n):
        uf.union(i, nums[i])
    res = []
    for i in range(n):
        rootI = uf.find(i)
        res.append(uf.caps[rootI])
    return res


a = [1, 2]
print(findSignatureCounts(a))

a = [2, 1]
print(findSignatureCounts(a))

a = [4, 3, 2, 5, 1]
print(findSignatureCounts(a))

a = [5, 1, 2, 3, 6, 4]
print(findSignatureCounts(a))
