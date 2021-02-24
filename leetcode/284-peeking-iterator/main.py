"""
  questions to ask:
  - will call next(), peek() after hasNext()? maybe
  - what is the definition/structure of the iterator?
"""

# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


"""
    1st: buffer?

    Time    O(1)
    Space   O(1)
    28 ms, faster than 16.67%
"""


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.buffer = None
        if self.iterator.hasNext():
            self.buffer = self.iterator.next()

    def peek(self):
        return self.buffer

    def next(self):
        res = self.buffer
        if self.iterator.hasNext():
            self.buffer = self.iterator.next()
        else:
            self.buffer = None
        return res

    def hasNext(self):
        return self.buffer != None
