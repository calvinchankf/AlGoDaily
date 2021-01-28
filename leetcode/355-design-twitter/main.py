import heapq

"""
    1st approach: 2 hashtable + hashset
    - save the users in the hashtable, and save their following users in a hashset
    e.g. connections = {
        'calvin': {'jack', 'jacky', 'bob'},
        'alice': {'peter', 'roy'},
        ...
    }
    - save the tweets with a userId
    e.g. news list = {
        'calvin': [(1,123), (2,323), (10,4334)],
        'jack': [(3,43), (5,3233)],
        ...
    }
    - every time we get the newsfeed of a user, we merge the followings tweets and sort them by its timestamp and return 10 most recent

    corner case:
    - a user cannot unfollow himself

    Time
    - postTweet O(1)
    - getNewsFeed (NlogN) N: all followings tweets
    - follow average O(1)
    - follow average O(1)
    Space   O(M+N) tweets + users conncections
    184 ms, faster than 31.79%
"""


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.news = {}
        self.connections = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # add user if necessary
        if userId not in self.connections:
            self.connections[userId] = set([userId])
        if userId not in self.news:
            self.news[userId] = []
        # append the tweet user
        self.news[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # return [] if no such user
        if userId not in self.connections:
            return []
        # get the followings
        followings = self.connections[userId]
        allTweets = []
        for user in followings:
            if user not in self.news:
                continue
            tweets = self.news[user]
            allTweets += tweets
        temps = sorted(allTweets, key=lambda x: x[0], reverse=True)
        res = []
        for temp in temps[:10]:
            res.append(temp[1])
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # add user if necesssary
        if followerId not in self.connections:
            self.connections[followerId] = set([followerId])
        # add a following
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # a user cannot unfollow himself
        if followerId == followeeId:
            return
        # unfollow a user
        if followerId in self.connections:
            if followeeId in self.connections[followerId]:
                self.connections[followerId].remove(followeeId)


"""
    2nd: same as 1st but with a minheap

    Time
    - postTweet O(1)
    - getNewsFeed (NlogK) N: all followings tweets, K=10
    - follow average O(1)
    - follow average O(1)
    Space   O(M+N) tweets + users conncections
    96 ms, faster than 41.94%
"""


class Twitter:

    def __init__(self):
        self.feeds = {}  # {userId: []}
        self.connections = {}  # {follower: set(followees)}
        self.timestamp = 0

    def _initUser(self, userId):
        if userId in self.feeds and userId in self.connections:
            return
        self.feeds[userId] = []
        self.connections[userId] = set([userId])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._initUser(userId)
        self.feeds[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.connections:
            return []
        tweets = []
        followings = self.connections[userId]
        for followee in followings:
            if followee not in self.feeds:
                continue
            for tweet in self.feeds[followee]:
                tweets.append(tweet)
        minheap = []
        for tweetId, timestamp in tweets:
            heappush(minheap, (timestamp, tweetId))
            if len(minheap) > 10:
                heappop(minheap)
        res = sorted(minheap, key=lambda x: -x[0])
        return [tweetId for timestamp, tweetId in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._initUser(followerId)
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.connections:
            return
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)
