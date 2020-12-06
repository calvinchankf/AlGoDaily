from heapq import *

"""
    There is a continous stream of data in the form of:
    Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")

    Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
    You cannot queue up the incoming data from the stream.
    So for example if the first incoming bit of data is (1, "abcd"), and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.

"""

"""
    Stream input

    questions:
    - no duplicate IDs?
    - no duplicate strings?
    - if we reach to z, should we rotate back to a?
    - can i assume, the s is in order? e.g. (1, "abcd") but bot (1, "abdc") ?
"""


class StreamDataInOrder(object):
    def __init__(self):
        self.cur = -1
        self.minheap = []

    def getData(self, oId, s):
        if self.cur == -1:
            self.cur = self._getCharIdx(s[-1])
            return [oId]

        res = []

        cIdx = self._getCharIdx(s[0])
        heappush(self.minheap, (cIdx, s, oId))
        print(self.cur, self.minheap)
        while len(self.minheap) > 0:
            if (self.cur + 1) % 26 == self.minheap[0][0]:
                _smallest, _s, _oId = heappop(self.minheap)
                self.cur = self._getCharIdx(_s[-1])
                res.append(_oId)
            else:
                break
        return res

    def _getCharIdx(self, c):
        return ord(c) - ord('a')


s = StreamDataInOrder()
print(s.getData(1, 'abcd'))
print(s.getData(2, 'efgh'))
print(s.getData(4, 'mnop'))
print(s.getData(5, 'qrst'))
print(s.getData(3, 'ijkl'))
print(s.getData(6, 'uvwxy'))
print(s.getData(7, 'zabcde'))
# this is the question i want to ask: ab comes before fghi..., so 8 never gets printed out
print(s.getData(9, 'ab'))
print(s.getData(8, 'fghijklmnopqrstuvwxyz'))

print("-----")

"""
    array input
    [(1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl"), (6, "xyz")]
    output: 1, 2, 3, 4, 5

    - similar to lc128
"""


def f(arr):
    res = []
    prefixHt = {}
    suffixHt = {}
    for oId, s in arr:
        prefixHt[s[0]] = (oId, s)
        suffixHt[s[-1]] = (oId, s)
    seen = set()
    for oId, s in arr:
        if oId in seen:
            continue
        seen.add(oId)

        temp = [oId]

        left = s[0]
        while chr(ord(left) - 1) in suffixHt:
            _oId, _s = suffixHt[chr(ord(left) - 1)]
            left = _s[0]
            seen.add(_oId)
            temp.insert(0, _oId)

        right = s[-1]
        while chr(ord(right) + 1) in prefixHt:
            _oId, _s = prefixHt[chr(ord(right) + 1)]
            right = _s[-1]
            seen.add(_oId)
            temp.append(_oId)

        if len(temp) > len(res):
            res = temp
    return res


a = [(1, "abcd"), (2, "efgh"), (4, "mnop"),
     (5, "qrst"), (3, "ijkl"), (6, "xyz")]
print(f(a))
