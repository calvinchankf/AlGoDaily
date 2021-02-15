import heapq
"""
    1st approach: 2 hashtable + minheap
    
    1. save the users in the hashtable, and save their following users in a hashset
    e.g. followship = {
        'calvin': {'jack', 'jacky', 'bob'},
        'alice': {'peter', 'roy'},
        ...
    }
    
    2. save the tweets with a userId
    e.g. userPosts = {
        'calvin': [(1,123), (2,323), (10,4334)],
        'jack': [(3,43), (5,3233)],
        ...
    }
    3. every time we get the newsfeed of a user, we merge the followings tweets and sort them by its timestamp and return 10 most recent

    corner cases:
    - a user cannot unfollow himself
    - a user cannot unfollow a user who is not a followee

    Time
    - postTweet         O(1)
    - getNewsFeed       O(NlogK) N : all followings tweets, K = 10 in this case
    - follow average    O(1), worst O(n) in a case where all the keys collide
    - follow average    O(1), worst O(n) in a case where all the keys collide
    Space   O(M+N) tweets + users conncections
    128 ms, faster than 26.27%
"""


class Twitter(object):

    def __init__(self):
        self.userPosts = {}     # { calvin: [(ada,1, (dad, 2), ...]
        self.followship = {}    # { calvin: [calvin, alice, bob]...}
        self.timestamp = 0

    def _initUser(self, userId):
        if userId in self.userPosts and userId in self.followship:
            return
        self.userPosts[userId] = []
        self.followship[userId] = set([userId])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._initUser(userId)
        self.userPosts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._initUser(userId)
        followings = self.followship[userId]
        minheap = []
        for f in followings:
            for time, tweetId in self.userPosts[f]:
                heappush(minheap, (time, tweetId))
                if len(minheap) > 10:
                    heappop(minheap)
        minheap.sort(key=lambda x: -x[0])
        return [x[1] for x in minheap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self._initUser(followerId)
        self._initUser(followeeId)
        self.followship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._initUser(followerId)
        self._initUser(followeeId)
        if followeeId in self.followship[followerId]:
            self.followship[followerId].remove(followeeId)
