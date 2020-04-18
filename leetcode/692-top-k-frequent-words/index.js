/*
    1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys
	3. put the hashtable key&value into a bucket with freq as an index
	4. the first k elements are the top k elements in the bucket

	Time	O(nlogn * klogk)
	Space	O(n)
	76 ms, faster than 47.07%
*/

/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function (words, k) {
	const ht = {};
	words.forEach((word) => {
		if (ht[word] === undefined) {
			ht[word] = 1;
		} else {
			ht[word] += 1;
		}
	});
	const arr = [];
	for (let key in ht) {
		arr.push([ht[key], key]);
	}
	arr.sort((a, b) => {
		if (a[0] === b[0]) {
			return a[1] < b[1] ? -1 : 1;
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
