/*
    1st approach
    - count num: freq into a hashtable
    - put the hashtable key&value into a priority queue
    - the first k elements are the top k elements in the priority queue

    56 ms, faster than 99.52%
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
	const ht = {};
	nums.forEach((num) => {
		if (ht[num] === undefined) {
			ht[num] = 1;
		} else {
			ht[num] += 1;
		}
	});
	const arr = [];
	for (let key in ht) {
		arr.push([ht[key], key]);
	}
	arr.sort((a, b) => {
		if (a[0] === b[0]) {
			return b[1] - a[1];
		}
		return b[0] - a[0];
	});
	const res = [];
	for (let pair of arr) {
		const [count, value] = pair;
		res.push(value);
		if (res.length == k) {
			break;
		}
	}
	return res;
};
