import bisect
from collections import defaultdict


"""
    1st: binary search

    Time    O(NlogN) -> O(N^2)
    Space   O(N)
    388 ms, faster than 25.00% 
"""


class TweetCounts(object):

    def __init__(self):
        self.ht = defaultdict(list)

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        arr = self.ht[tweetName]
        bisect.insort_right(arr, time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        m = {
            'minute': 60,
            'hour': 3600,
            'day': 216000,
        }
        arr = self.ht[tweetName]
        res = []
        while startTime <= endTime:
            to = min(startTime + m[freq], endTime + 1)

            i = bisect.bisect_left(arr, startTime)
            j = bisect.bisect_left(arr, to)
            res.append(j-i)

            startTime += m[freq]
        return res


obj = TweetCounts()
obj.recordTweet('tweet3', 0)
obj.recordTweet('tweet3', 60)
obj.recordTweet('tweet3', 10)
print(obj.getTweetCountsPerFrequency('minute', 'tweet3', 0, 59))
print(obj.getTweetCountsPerFrequency('minute', 'tweet3', 0, 60))
obj.recordTweet("tweet3", 120)
print(obj.getTweetCountsPerFrequency('hour', 'tweet3', 0, 210))

print("----")

obj = TweetCounts()
obj.recordTweet('tweet0', 33)
obj.recordTweet('tweet1', 89)
obj.recordTweet('tweet2', 99)
obj.recordTweet('tweet3', 53)
obj.recordTweet('tweet4', 4)
print(obj.getTweetCountsPerFrequency('day', 'tweet0', 89, 3045))

print("----")

obj = TweetCounts()
obj.recordTweet('tweet0', 13)
obj.recordTweet('tweet1', 16)
obj.recordTweet('tweet2', 12)
obj.recordTweet('tweet3', 18)
obj.recordTweet('tweet3', 89)
obj.recordTweet('tweet4', 82)
print(obj.getTweetCountsPerFrequency('day', 'tweet0', 89, 9471))
print(obj.getTweetCountsPerFrequency('hour', 'tweet3', 13, 4024))

print("----")

["TweetCounts", "recordTweet", "recordTweet", "recordTweet", "recordTweet", "recordTweet", "getTweetCountsPerFrequency",
    "getTweetCountsPerFrequency", "getTweetCountsPerFrequency", "getTweetCountsPerFrequency"]
[[], ["tweet0", 857105800], ["tweet1", 255428777], ["tweet2", 13881700], ["tweet3", 82366032], ["tweet4", 334311127], ["minute", "tweet0",
                                                                                                                       255428777, 255438544], ["day", "tweet2", 857105800, 857108372], ["minute", "tweet4", 334311127, 334316350], ["hour", "tweet3", 82366032, 82370980]]

obj = TweetCounts()
obj.recordTweet('tweet0', 857105800)
obj.recordTweet('tweet1', 255428777)
obj.recordTweet('tweet2', 13881700)
obj.recordTweet('tweet3', 82366032)
obj.recordTweet('tweet4', 334311127)
# print(obj.getTweetCountsPerFrequency('minute', 'tweet0', 857105800, 255438544))
print(obj.getTweetCountsPerFrequency('minute', 'tweet0', 255428777, 255438544))
print(obj.getTweetCountsPerFrequency('day', 'tweet2', 857105800, 857108372))
print(obj.getTweetCountsPerFrequency('minute', 'tweet4', 334311127, 334316350))
print(obj.getTweetCountsPerFrequency('hour', 'tweet3', 82366032, 82370980))
