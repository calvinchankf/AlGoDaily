"""
    1st approach: hashtable

    Time    O(1)
    Space   O(n)
    136 ms, faster than 51.26%
"""


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.ht:
            prev = self.ht[message]
            if timestamp < prev + 10:
                return False
        self.ht[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
