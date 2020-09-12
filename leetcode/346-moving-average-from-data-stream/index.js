/*
    1st approach: sliding window

    Time    O(1) next()
    Space   O(k) k: size since we need to store the sliding window
    56 ms, faster than 70.34%
*/
var MovingAverage = function (size) {
	this.window = [];
	this.total = 0;
	this.size = size;
};

/**
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function (val) {
	this.window.push(val);
	this.total += val;
	if (this.window.length > this.size) {
		const last = this.window.shift();
		this.total -= last;
	}
	return this.total / this.window.length;
};
