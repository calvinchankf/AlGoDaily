/*
    1st approach: hashtable

    Time    O(2n)
    Space   O(n)
    80 ms, faster than 74.16%
*/
var majorityElement = function (nums) {
	const n = nums.length;
	const ht = {};
	for (let x of nums) {
		if (x in ht) {
			ht[x] += 1;
		} else {
			ht[x] = 1;
		}
	}
	const res = [];
	for (let k in ht) {
		if (ht[k] > n / 3) {
			res.push(k);
		}
	}
	return res;
};
