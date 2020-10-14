"""
    1st approach: hashtables
    - 1 hashtable act as a counter
    - 1 hashtable stores the array of values at occurence at key

    e.g. [5,7,5,7,4,5]
    
    counter [val1: occurence1, val2: occurence2, ...]
    {
      5:3
      7:2
      4:1
    }

    map of occurence: [val1, val2,...]
    {
      3: [5],
      2: [7, 5, 7]
      1: [5, 4]
    }

    when we pop, we pop the 5 from 3: [5] such that

    counter [val1: occurence1, val2: occurence2, ...]
    {
      5:2
      7:2
      4:1
    }

    map of occurence: [val1, val2,...]
    {
      2: [7, 5, 7]
      1: [5, 4]
    }

    when we pop again, we pop the 7 from 2: [7, 5, 7] such that

    counter [val1: occurence1, val2: occurence2, ...]
    {
      5:2
      7:1
      4:1
    }

    map of occurence: [val1, val2,...]
    {
      2: [7, 5]
      1: [5, 4]
    }

    Time    O(1)
    Space   O(n)
    372 ms, faster than 39.67%
"""


class FreqStack(object):

    def __init__(self):
        self.counter = {}
        self.map = {}
        self.maxFreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x not in self.counter:
            self.counter[x] = 1
        else:
            self.counter[x] += 1
        occurence = self.counter[x]
        self.maxFreq = max(self.maxFreq, occurence)

        if occurence not in self.map:
            self.map[occurence] = [x]
        else:
            self.map[occurence].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.map[self.maxFreq].pop()
        if len(self.map[self.maxFreq]) == 0:
            del self.map[self.maxFreq]
            self.maxFreq -= 1
        self.counter[x] -= 1
        if self.counter[x] == 0:
            del self.counter[x]
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

"""
    2nd approach: optimize the 1st approach to use an array for frequency

    Time    O(1)
    Space   O(n)
    356 ms, faster than 50.80%
"""


from collections import Counter

class FreqStack(object):

    def __init__(self):
        self.counter = Counter()
        self.freqs = []

    def push(self, x):
        self.counter[x] += 1
        idx = self.counter[x] - 1
        if idx == len(self.freqs):
            self.freqs.append([x])
        else:
            self.freqs[idx].append(x)
        

    def pop(self):
        freqArr = self.freqs[-1]
        x = freqArr.pop()
        self.counter[x] -= 1
        if len(freqArr) == 0:
            self.freqs.pop()
        if self.counter[x] == 0:
            del self.counter[x]
        return x
