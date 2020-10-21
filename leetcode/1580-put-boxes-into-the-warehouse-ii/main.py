import sys

"""
    1st: sort + prefix min + 2 pointers
    - sort the boxes
    - record the running prefix min from 2 ends
    - split the warehouse from according to the prefix mins
    - put the boxes into the warehouseA(forward) and warehouseB(backward) accrodingly

    e.g.
    boxes = [3,7,4,5,1,6,13,7]
    warehouse = [12,7,16,15,10,16,6,4,6,16,8,8,9]

    1. sort the boxes [1, 3, 4, 5, 6, 7, 7, 13]

    2. prefix min from 2 ends
    forward [12,7,7,7,7,7,6,4,4,4,4,4,4]
    backward [4,4,4,4,4,4,4,4,6,8,8,8,9]
                            ^split here

    3. so warehouse can be split into:
    forward     = [6, 7, 7, 7, 7, 7, 12]
    backward    = [4, 6, 8, 8, 8, 9]

    put the boxes into forward or backward
    forward     = [6, 7, 7, 7, 7, 7, 12]
    boxes       = [3, 5, 6, 7]  <- 4 boxes

    backward    = [4, 6, 8, 8, 8, 9]
    boxes       = [1, 4, 7]     <- 3 boxes

    At the end, we can place 4 + 3 = 7 boxes

"""


class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        n = len(warehouse)
        forward = n * [sys.maxsize]
        backward = n * [sys.maxsize]
        curMin = sys.maxsize
        for i in range(n):
            curMin = min(curMin, warehouse[i])
            forward[i] = curMin
        curMin = sys.maxsize
        for i in range(n-1, -1, -1):
            curMin = min(curMin, warehouse[i])
            backward[i] = curMin
        for i in range(n):
            if warehouse[i] == curMin:
                forward = forward[:i]
                backward = backward[i:]
                break
        forward = forward[::-1]
        boxes.sort()
        # print(forward, backward)
        # print(boxes)
        res = 0
        i = 0
        j = 0
        # temp = []
        for box in boxes:
            while i < len(forward) and forward[i] < box:
                i += 1
            while j < len(backward) and backward[j] < box:
                j += 1
            if i < len(forward) and j < len(backward):
                if forward[i] < backward[j]:
                    # temp.append((box, forward[i], 'f'))
                    res += 1
                    i += 1
                else:
                    # temp.append((box, backward[j], 'b'))
                    res += 1
                    j += 1
            elif i < len(forward):
                # temp.append((box, forward[i], 'f'))
                res += 1
                i += 1
            elif j < len(backward):
                # temp.append((box, backward[j], 'b'))
                res += 1
                j += 1
        # print(temp)
        return res


s = Solution()


a = [3, 7, 4, 5, 1, 6, 13, 7]
b = [12, 7, 16, 15, 10, 16, 6, 4, 6, 16, 8, 8, 9]

s.maxBoxesInWarehouse(a, b)
