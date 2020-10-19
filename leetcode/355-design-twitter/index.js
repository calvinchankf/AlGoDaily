/*
    2nd approach: 2 hashtable + hashset
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
    - getNewsFeed (nlogn) n: all followings tweets
    - follow average O(1), worst O(n) in a case where all the keys collide
    - follow average O(1), worst O(n) in a case where all the keys collide
    Space   O(M+N) tweets + users conncections
    116 ms, faster than 98.75%
*/
var Twitter = function () {
	this.followings = {};
	this.newsfeeds = {};
	this.timestamp = 0;
};

/**
 * Compose a new tweet.
 * @param {number} userId
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function (userId, tweetId) {
	if (userId in this.followings === false) {
		this.followings[userId] = new Set([userId]);
	}
	if (userId in this.newsfeeds == false) {
		this.newsfeeds[userId] = [];
	}
	this.newsfeeds[userId].push([this.timestamp, tweetId]);
	this.timestamp += 1;
};

/**
 * Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function (userId) {
	if (userId in this.followings === false) {
		return [];
	}
	const people = this.followings[userId];
	let res = [];
	for (let p of people) {
		if (p in this.newsfeeds) {
			const tweetes = this.newsfeeds[p];
			res = res.concat(tweetes);
		}
	}
	res.sort((a, b) => b[0] - a[0]);
	return res.slice(0, 10).map((x) => x[1]);
};

/**
 * Follower follows a followee. If the operation is invalid, it should be a no-op.
 * @param {number} followerId
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function (followerId, followeeId) {
	if (followerId in this.followings === false) {
		this.followings[followerId] = new Set([followerId]);
	}

	if (followerId in this.followings) {
		this.followings[followerId].add(followeeId);
	} else {
		this.followings[followerId] = new Set([followeeId]);
	}
};

/**
 * Follower unfollows a followee. If the operation is invalid, it should be a no-op.
 * @param {number} followerId
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function (followerId, followeeId) {
	if (followerId === followeeId) {
		return;
	}

	if (followerId in this.followings) {
		if (this.followings[followerId].has(followeeId)) {
			this.followings[followerId].delete(followeeId);
		}
	}
};

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = Object.create(Twitter).createNew()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
