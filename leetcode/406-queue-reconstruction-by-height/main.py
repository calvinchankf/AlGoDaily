"""
    1st: sort + queue
    - first sort the input in a reversed order
    - then put the each person into a correct position

    e.g. [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sort the input: [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    
    1st iteration: [7, 0]
    remaining: [[7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    
    2nd iteration: [[7, 0], [7, 1]]
    remaining: [[6, 1], [5, 0], [5, 2], [4, 4]]
    
    3rd iteration: [[7, 0], [6, 1], [7, 1]]
    remaining: [[5, 0], [5, 2], [4, 4]]
    
    4th iteration: [[5, 0], [7, 0], [6, 1], [7, 1]]
    remaining: [[4, 4], [5, 2]]

    5th iteration: [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
    remaining: [[4, 4]]

    final iteration: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def cptr(a, b):
            if a[0] == b[0]:
                return b[1]-a[1]
            return a[0]-b[0]
        people = sorted(people, cmp=cptr, reverse=True)
        res = []
        while len(people) > 0:
            h, k = people.pop(0)

            if k == 0:
                res.insert(0, [h, k])
                continue

            count = 0
            for i in range(len(res)):
                if res[i][0] >= h:
                    count += 1
                if count == k:
                    res.insert(i+1, [h, k])
                    break
        return res
