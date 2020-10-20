/*
    4th approach: upper bound binary search
    - add the number in correct position
    - find median from the half of the array

    Time of addNum()        O(n) because list.insert() takes O(n)
    Space of findMedian()   O(n)
    244 ms, faster than 94.54%
*/

/**
 * initialize your data structure here.
 */
var MedianFinder = function () {
	this.nums = [];
};

/**
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function (num) {
	const i = upperBsearch(this.nums, num);
	this.nums.splice(i, 0, num);
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function () {
	if (this.nums.length % 2 == 0) {
		const half = Math.floor(this.nums.length / 2);
		const left = this.nums[half - 1];
		const right = this.nums[half];
		return (left + right) / 2;
	}
	const half = Math.floor(this.nums.length / 2);
	return this.nums[half];
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */

const upperBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};
