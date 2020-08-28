/*
    2nd approach:
    - dont use OrderedDict, use a hashtable + array to do the same thing
    - hit() => put the keys in the hashtable, increment the count for existing keys
    - getHits() => count the result by iterating through the hashtable from back until the key <= timestamp - 300

    Time of hit()       O(1)
    Time of getHits()   O(1) cos it just counts 300 keys at maximum
    Space   O(n)
    76 ms, faster than 49.52%
*/

/**
 * Initialize your data structure here.
 */
var HitCounter = function () {
	this.ht = {};
	this.nums = [];
};

/**
 * Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). 
 * @param {number} timestamp
 * @return {void}
 */
HitCounter.prototype.hit = function (timestamp) {
	if (!(timestamp in this.ht)) {
		this.ht[timestamp] = 1;
		this.nums.push(timestamp);
	} else {
		this.ht[timestamp] += 1;
	}
};

/**
 * Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). 
 * @param {number} timestamp
 * @return {number}
 */
HitCounter.prototype.getHits = function (timestamp) {
	let res = 0;
	const n = this.nums.length;
	let deleteUntil = -1;
	for (let i = n - 1; i >= 0; i--) {
		const key = this.nums[i];
		// const keyStr = parseInt(key)
		const count = this.ht[key];
		if (timestamp - key < 300) {
			res += count;
		} else {
			delete this.ht[key];
			if (deleteUntil === -1) {
				deleteUntil = i;
			}
		}
	}
	this.nums = this.nums.slice(deleteUntil + 1);
	return res;
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * var obj = new HitCounter()
 * obj.hit(timestamp)
 * var param_2 = obj.getHits(timestamp)
 */
